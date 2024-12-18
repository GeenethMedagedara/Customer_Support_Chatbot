"""
Test cases for API endpoints using pytest and FastAPI test client.
"""
import pytest
import asyncio
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def event_loop():
    """
     Provide an event loop for asyncio tests.
    """
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
def test_restart_chatbot():
    """
    Test the /restart/ endpoint to verify that the chatbot restart functionality works as expected.
    """
    response = client.post("/restart/", json={"sender": "ghost"})
    assert response.status_code == 200
    assert response.json() == {"message":"Chat restarted successfully"}
    print("Chatbot restart: SUCCESSFUL 1")

@pytest.mark.asyncio
def test_chat_with_chatbot():
    """
    Test the /chat/ endpoint to verify chatbot conversation handling.
    """
    response = client.post("/chat/", json={"sender": "test", "message": "thankyou"})
    assert response.status_code == 200

    # Extract the response JSON
    response_data = response.json()

    # Expected response without timestamp check
    expected_message = {
        "sender": "bot",
        "message": "Your welcome",
    }

    # Validate response excluding timestamp
    assert response_data[0]["sender"] == expected_message["sender"]
    assert response_data[0]["message"] == expected_message["message"]
    assert "timestamp" in response_data[0]
    print("Chatbot conversation:  2")

@pytest.mark.asyncio
def test_order_status():
    """
    Test the /value/ endpoint to verify status of the order.
    """
    response = client.post("/value/", json={"order_id": "1234567890"})
    assert response.status_code == 200
    assert response.json() == {'order_id': 1234567890, 'name': 'Test set', 'qty': 1, 'status': 'test', 'total': 1000.0}
    print("Check order status: SUCCESSFUL 3")

@pytest.mark.asyncio
def test_sorting_unique_categories():
    """
    Test the /sort/ endpoint to verify sorting of unique categories.
    """
    response = client.post("/sort/")
    assert response.status_code == 200
    print("Sorting unique categories: SUCCESSFUL 4")

@pytest.mark.asyncio
def test_getting_latest_session():
    """
        Test the /session/ endpoint to verify retrieving last session.
    """
    response = client.post("/session/", json={"sender": "test"})
    assert response.status_code == 200
    print("Retrieving latest session: SUCCESSFUL 5")

@pytest.mark.asyncio
def test_getting_items_by_category():
    """
    Test the /category/ endpoint to verify getting items by categories.
    """
    response = client.post("/category/", json={"category": "Table"})
    assert response.status_code == 200
    print("Retrieving items by category: SUCCESSFUL 6")

@pytest.mark.asyncio
def test_chatgpt():
    """
    Test the /gpt/ endpoint to verify gpt works.
    """
    response = client.post("/gpt/", json={"message": "This just a test to test my fastapi server"})
    assert response.status_code == 200
    print("ChatGPT availability: SUCCESSFUL 7")
