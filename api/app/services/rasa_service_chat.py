"""
Service functions to converse with rasa server from fastapi
"""
import httpx

"""
The normal url for rasa server is http://localhost:5005/webhooks/rest/webhook   etc... but wen dockerised use http://host.docker.internal:5005/webhooks/rest/webhook
"""

async def send_message_to_rasa(sender: str, message: str):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://host.docker.internal:5005/webhooks/rest/webhook", json={"sender": sender, "message": message})
        response.raise_for_status()
        return response.json()

async def get_tracker(sender: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://host.docker.internal:5005/conversations/{sender}/tracker")
        response.raise_for_status()
        return response.json()
