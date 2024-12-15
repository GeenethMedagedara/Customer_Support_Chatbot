from fastapi import APIRouter, HTTPException
from datetime import datetime, timezone, timedelta
from api.schemas.message_chat import Message
from api.services.rasa_service_chat import send_message_to_rasa, get_tracker
from api.services.db.dynamodb_service_chat import create_dynamodb_client, store_conversation, update_conversation
from api.config import settings

router = APIRouter()

@router.post("/chat/")
async def chat_with_rasa(message: Message):
    try:
        # Interact with Rasa
        rasa_response = await send_message_to_rasa(message.sender, message.message)
        tracker_data = await get_tracker(message.sender)
        slots = tracker_data.get("slots", {})
        current_timestamp = datetime.now(timezone.utc).isoformat()

        # Prepare messages for DynamoDB
        bot_messages = [
            {"M": {
                "sender": {"S": "bot"},
                "message": {"S": res["text"]},
                "timestamp": {"S": current_timestamp}
            }} for res in rasa_response
        ]
        user_message = {
            "M": {
                "sender": {"S": "user"},
                "message": {"S": message.message},
                "timestamp": {"S": current_timestamp}
            }
        }

        # Interact with DynamoDB
        async with await create_dynamodb_client() as dynamodb:
            response = await dynamodb.query(
                TableName=settings.DYNAMODB_TABLE_CHAT,
                KeyConditionExpression="conversation_id = :conversation_id",
                ExpressionAttributeValues={":conversation_id": {"S": message.sender}}
            )
            if "Items" not in response or len(response["Items"]) == 0:
                # New conversation
                await store_conversation(
                    dynamodb, settings.DYNAMODB_TABLE_CHAT, message.sender,
                    current_timestamp, slots, [user_message] + bot_messages
                )
            else:
                latest_item = max(response["Items"], key=lambda x: x["created_at"]["S"])
                created_at = latest_item["created_at"]["S"]
                time_difference = datetime.now(timezone.utc) - datetime.fromisoformat(created_at.replace("Z", "+00:00"))

                if time_difference >= timedelta(minutes=5):
                    # Start a new conversation
                    await store_conversation(
                        dynamodb, settings.DYNAMODB_TABLE_CHAT, message.sender,
                        current_timestamp, slots, [user_message] + bot_messages
                    )
                else:
                    # Update existing conversation
                    await update_conversation(
                        dynamodb, settings.DYNAMODB_TABLE_CHAT, message.sender,
                        created_at, slots, [user_message] + bot_messages
                    )

        # Return response
        return [{"sender": "bot", "message": res["text"], "timestamp": datetime.now(timezone.utc).isoformat()} for res in rasa_response]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
