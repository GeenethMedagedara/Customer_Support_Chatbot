async def get_order_from_dynamodb(client, table_name: str, order_id: int):
    """Fetch an order item from the DynamoDB table."""
    response = await client.get_item(
        TableName=table_name,
        Key={"order_id": {"N": str(order_id)}}
    )
    return response.get("Item")
