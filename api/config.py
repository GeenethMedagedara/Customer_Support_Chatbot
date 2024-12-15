from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    DYNAMODB_TABLE_CHAT: str = "Conversations"
    DYNAMODB_TABLE_CAT_SORT: str = "Product"
    DYNAMODB_TABLE_VALUE: str = "Orders"
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    OPENAI_API_KEY: str

    class Config:
        env_file = str(Path(__file__).parent.parent / ".env")


settings = Settings()
