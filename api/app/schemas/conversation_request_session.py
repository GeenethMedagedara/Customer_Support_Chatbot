from pydantic import BaseModel

class ConversationRequest(BaseModel):
    sender: str
