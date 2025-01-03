"""
Function handles the routing for getting gpt response
"""
from fastapi import APIRouter, HTTPException

#Paths
from ..schemas.message_request_gpt import MessageRequest  # Import the BaseModel
from ..config import settings
from ..services.openai_service_gpt import call_openai_api

router = APIRouter()

@router.post("/gpt/")
async def ask_chat_gpt(request: MessageRequest):
    try:
        # Call the helper function
        gpt_response = await call_openai_api(settings.OPENAI_API_KEY, request.message)
        return {"response": gpt_response}
    except HTTPException as exc:
        raise exc  # Pass through HTTP exceptions for proper error handling
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {exc}")
