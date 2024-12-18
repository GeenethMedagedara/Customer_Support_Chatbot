"""
Service functions for the chatgpt api
"""
import httpx
from fastapi import HTTPException

async def call_openai_api(api_key: str, user_message: str) -> str:
    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 150,
        "temperature": 0.7,
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(openai_url, json=payload, headers=headers, timeout=10.0)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=500, detail=f"An error occurred: {exc}")
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=f"API error: {exc.response.text}")
