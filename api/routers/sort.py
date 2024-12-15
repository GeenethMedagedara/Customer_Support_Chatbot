from api.config import settings
from fastapi import APIRouter, HTTPException
from aiobotocore.session import get_session
from typing import List
from api.services.db.dynamodb_scan_table_sort import scan_table
from api.services.extract_unique_categories_sort import extract_unique_categories

router = APIRouter()

@router.post("/sort/", response_model=List[str])
async def get_unique_categories():
    async with get_session().create_client(
        'dynamodb',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    ) as dynamodb_client:
        try:
            items = await scan_table(dynamodb_client, settings.DYNAMODB_TABLE_CAT_SORT)
            categories = await extract_unique_categories(items)
            return categories
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching categories: {str(e)}")