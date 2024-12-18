from contextlib import asynccontextmanager
from aiobotocore.session import get_session
from api.config import settings

@asynccontextmanager
async def get_dynamodb_client():
    """
    Asynchronous context manager to create and yield a DynamoDB client using aiobotocore.
    """
    session = get_session()
    async with session.create_client(
        "dynamodb",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION,
    ) as client:
        yield client
