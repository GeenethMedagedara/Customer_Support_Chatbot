"""
Function handles the routing for getting the last session
"""
from fastapi import APIRouter, HTTPException
from api.schemas.conversation_request_session import ConversationRequest
from api.services.dynamodb_json_to_normal_json_session import dynamodb_json_to_normal_json
from api.services.send_slots_to_rasa_session import send_slots_to_rasa
from api.services.process_recent_conversation_session import process_recent_conversation
from api.config import settings
from aiobotocore.session import get_session
from api.utils.aws_client import get_dynamodb_client

router = APIRouter()

@router.post("/session/")
async def get_recent_conversation(request: ConversationRequest):
    async with get_dynamodb_client() as dynamodb_client:
        try:
            # Fetch the recent conversation
            latest_item = await process_recent_conversation(
                dynamodb_client, settings.DYNAMODB_TABLE_CHAT, request.sender
            )

            if latest_item:
                # Convert to standard JSON
                normal_json = dynamodb_json_to_normal_json(latest_item)

                # Extract and send slots to Rasa
                slots = normal_json.get("slots", {})
                await send_slots_to_rasa(request.sender, slots)

                return normal_json
            else:
                return {"message": "No recent conversation found within the last 5 minutes."}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
