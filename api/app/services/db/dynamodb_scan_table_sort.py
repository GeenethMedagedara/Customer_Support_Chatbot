"""
DB function to scan table name and get values
"""
async def scan_table(client, table_name: str):
    """Scans a DynamoDB table and handles pagination."""
    items = []
    response = await client.scan(TableName=table_name)
    items.extend(response.get("Items", []))

    # Handle pagination
    while "LastEvaluatedKey" in response:
        response = await client.scan(
            TableName=table_name,
            ExclusiveStartKey=response["LastEvaluatedKey"]
        )
        items.extend(response.get("Items", []))

    return items