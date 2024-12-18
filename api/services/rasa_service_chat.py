"""
Service functions to converse with rasa server from fastapi
"""
import httpx
from api.config import settings

async def send_message_to_rasa(sender: str, message: str):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:5005/webhooks/rest/webhook", json={"sender": sender, "message": message})
        response.raise_for_status()
        return response.json()

async def get_tracker(sender: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:5005/conversations/{sender}/tracker")
        response.raise_for_status()
        return response.json()
