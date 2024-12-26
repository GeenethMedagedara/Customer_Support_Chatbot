"""
Used to transform all from normal json to dynamodb json
"""
from typing import Dict

#Paths
from ..schemas.order_request_value import Order

async def transform_dynamodb_item_to_order(item: Dict) -> Order:
    """Convert a DynamoDB item to an Order Pydantic model."""
    return Order(
        order_id=int(item["order_id"]["N"]),
        name=item["name"]["S"],
        qty=int(item["qty"]["N"]),
        status=item["status"]["S"],
        total=float(item["total"]["N"]),
    )
