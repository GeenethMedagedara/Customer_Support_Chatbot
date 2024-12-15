async def filter_items_by_category(client, table_name: str, category: str):
    """Scans a table to filter items by category."""
    response = await client.scan(
        TableName=table_name,
        FilterExpression="category = :category",
        ExpressionAttributeValues={":category": {"S": category}},
    )
    return response.get("Items", [])