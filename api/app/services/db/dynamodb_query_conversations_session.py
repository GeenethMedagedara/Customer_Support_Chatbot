"""
Service function used to get the session id
"""
async def query_conversations(client, table_name: str, conversation_id: str):
    """Query DynamoDB for conversations by conversation_id."""
    return await client.query(
        TableName=table_name,
        KeyConditionExpression="conversation_id = :conversation_id",
        ExpressionAttributeValues={":conversation_id": {"S": conversation_id}}
    )
