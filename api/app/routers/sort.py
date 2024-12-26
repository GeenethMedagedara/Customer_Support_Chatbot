"""
Function handles the routing for sorting unique category values
"""
from fastapi import APIRouter, HTTPException
from typing import List

#Paths
from ..config import settings
from ..services.db.dynamodb_scan_table_sort import scan_table
from ..services.extract_unique_categories_sort import extract_unique_categories
from ..utils.aws_client import get_dynamodb_client

router = APIRouter()

@router.post("/sort/", response_model=List[str])
async def get_unique_categories():
    async with get_dynamodb_client() as dynamodb_client:
        try:
            items = await scan_table(dynamodb_client, settings.DYNAMODB_TABLE_CAT_SORT)
            categories = await extract_unique_categories(items)
            return categories
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching categories: {str(e)}")