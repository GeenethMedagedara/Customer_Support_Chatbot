from fastapi import APIRouter, HTTPException
from api.config import settings
from aiobotocore.session import get_session
from typing import List
from api.schemas.product_request_category_sort import Product, ProductRequest
from api.services.transform_dynamodb_items_to_products_category import transform_dynamodb_items_to_products
from api.services.db.dynamodb_filter_items_category import filter_items_by_category
from api.utils.aws_client import get_dynamodb_client

router = APIRouter()

@router.post("/category/", response_model=List[Product])
async def get_items_by_category(product_request: ProductRequest):
    # async with get_session().create_client(
    #     'dynamodb',
    #     aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    #     aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    #     region_name=settings.AWS_REGION
    # ) as dynamodb_client:
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