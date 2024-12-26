"""
Service function to set session slot back in the rasa chatbot
"""
import httpx
from typing import Dict

"""
The normal url for rasa server is http://localhost:5005/webhooks/rest/webhook   etc... but when dockerised use http://host.docker.internal:5005/webhooks/rest/webhook
"""

async def send_slots_to_rasa(conversation_id: str, slots: Dict):
    """Send slots to Rasa as SlotSet events."""
    async with httpx.AsyncClient() as client:
        for slot_name, slot_value in slots.items():
            await client.post(
                f"http://host.docker.internal:5005/conversations/{conversation_id}/tracker/events",
                json={"event": "bot", "name": slot_name, "value": slot_value}
            )
