"""
Function handles the routing for getting order status
"""
from fastapi import APIRouter, HTTPException
from api.config import settings
from api.schemas.order_request_value import OrderRequest, Order
from api.services.transform_dynamodb_item_to_order_value import transform_dynamodb_item_to_order
from api.services.db.dynamodb_get_order_value import get_order_from_dynamodb
from aiobotocore.session import get_session
from api.utils.aws_client import get_dynamodb_client

router = APIRouter()

@router.post("/value/", response_model=Order)
async def get_order(order_request: OrderRequest):
    async with get_dynamodb_client() as dynamodb_client:
        try:
            # Fetch item from DynamoDB
            item = await get_order_from_dynamodb(
                dynamodb_client, settings.DYNAMODB_TABLE_VALUE, order_request.order_id
            )

            if not item:
                raise HTTPException(status_code=404, detail="Item not found")

            # Transform item to Order model
            order = await transform_dynamodb_item_to_order(item)
            return order

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving item: {str(e)}")
