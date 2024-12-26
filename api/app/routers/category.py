"""
Function handles the routing for getting items by category
"""
from fastapi import APIRouter, HTTPException
from typing import List

#Paths
from ..config import settings
from ..schemas.product_request_category_sort import Product, ProductRequest
from ..services.transform_dynamodb_items_to_products_category import transform_dynamodb_items_to_products
from ..services.db.dynamodb_filter_items_category import filter_items_by_category
from ..utils.aws_client import get_dynamodb_client

router = APIRouter()

@router.post("/category/", response_model=List[Product])
async def get_items_by_category(product_request: ProductRequest):
    async with get_dynamodb_client() as dynamodb_client:
        try:
            items = await filter_items_by_category(
                dynamodb_client, settings.DYNAMODB_TABLE_CAT_SORT, product_request.category
            )
            if not items:
                raise HTTPException(status_code=404, detail="No items found in the specified category")

            products = await transform_dynamodb_items_to_products(items)
            return products
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving items: {str(e)}")