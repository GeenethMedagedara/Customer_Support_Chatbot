"""
Handles all the service functionality for chatbot conversation
"""
from datetime import datetime, timezone
import aiobotocore.session

#Paths
from ...config import settings

async def create_dynamodb_client():
    """
    Dynamodb client creation
    """
    return aiobotocore.session.get_session().create_client(
        'dynamodb',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )

async def store_conversation(client, table, conversation_id, created_at, slots, messages):
    """
    Storing conversations to recall later as sessions
    """
    await client.put_item(
        TableName=table,
        Item={
            "conversation_id": {"S": conversation_id},
            "created_at": {"S": created_at},
            "slots": {"M": {key: {"S": str(value)} for key, value in slots.items()}},
            "messages": {"L": messages},
            "last_updated": {"S": created_at}
        }
    )

async def update_conversation(client, table, conversation_id, created_at, slots, new_messages):
    """
    Update the stored conversation
    """
    await client.update_item(
        TableName=table,
        Key={
            "conversation_id": {"S": conversation_id},
            "created_at": {"S": created_at}
        },
        UpdateExpression="SET messages = list_append(messages, :new_messages), slots = :new_slots, last_updated = :updated_time",
        ExpressionAttributeValues={
            ":new_messages": {"L": new_messages},
            ":new_slots": {"M": {key: {"S": str(value)} for key, value in slots.items()}},
            ":updated_time": {"S": datetime.now(timezone.utc).isoformat()}
        }
    )
