"""
Service function to restart chatbot
"""
import httpx
from fastapi import HTTPException


async def send_restart_event(sender: str):
    """Send a restart event to the Rasa tracker for a specific sender."""
    payload = {"event": "restart"}
    url = f"http://localhost:5005/conversations/{sender}/tracker/events"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            return {"message": "Chat restarted successfully"}
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Rasa: {str(e)}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Rasa API error: {e.response.text}")
