"""
Function handles the routing for restarting the chatbot
"""
from fastapi import APIRouter
from api.schemas.rmessage_restart import Rmessage
from api.services.send_restart_event_restart import send_restart_event

router = APIRouter()

@router.post("/restart/")
async def restart_chat(message: Rmessage):
    """Restart the chat session for a given sender."""
    return await send_restart_event(message.sender)
