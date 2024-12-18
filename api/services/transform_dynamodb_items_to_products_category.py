"""
Used to transform all from dynamodb json to normal json
"""
from typing import List, Dict
from api.schemas.product_request_category_sort import Product

async def transform_dynamodb_items_to_products(items: List[Dict]) -> List[Product]:
    """Transform DynamoDB items to Product Pydantic models."""
    return [
        Product(
            product_id=int(item["product_id"]["N"]),
            category=item["category"]["S"],
            description=item["description"]["S"],
            name=item["name"]["S"],
            price=float(item["price"]["N"]),
            quantity=int(item["quantity"]["N"]),
            rating=float(item["rating"]["N"]),
            status=item["status"]["S"],
        )
        for item in items
    ]