from datetime import datetime, timezone, timedelta
from api.services.db.dynamodb_query_conversations_session import query_conversations
from fastapi import HTTPException


async def process_recent_conversation(client, table_name: str, conversation_id: str):
    """Process and retrieve the most recent conversation."""
    # Query DynamoDB
    response = await query_conversations(client, table_name, conversation_id)

    if "Items" not in response or len(response["Items"]) == 0:
        raise HTTPException(status_code=404, detail="No conversation found with the given conversation_id.")

    # Find the most recent conversation
    latest_item = max(
        response["Items"],
        key=lambda x: datetime.fromisoformat(x["created_at"]["S"].replace("Z", "+00:00"))
    )

    # Time difference calculation
    created_at = latest_item["created_at"]["S"]
    created_at_datetime = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    current_datetime = datetime.now(timezone.utc)
    time_difference = current_datetime - created_at_datetime

    return latest_item if time_difference < timedelta(minutes=5) else None
