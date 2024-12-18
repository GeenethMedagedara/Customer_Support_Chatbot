"""
The following functions tests the main processes of the rasa actions server
"""
import pytest
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from ..actions import ActionSayOrderStatus
from ..actions import ActionSayProductInquiry
from ..actions import ActionSayCategoryData

@pytest.fixture
def dispatcher():
    """Fixture for creating a dispatcher instance."""
    return CollectingDispatcher()

"""
Testing functions related to ordering 
"""
@pytest.fixture
def tracker_with_order_number():
    """Tracker with a pre-filled order number slot."""
    return Tracker(
        sender_id="test_user",
        slots={"order_no_value": "1122334455"},
        latest_message={"intent": {"name": "order_number"}},
        events=[],
        paused=False,
        followup_action=None,
        active_loop=None,
        latest_action_name="action_listen"
    )

@pytest.fixture
def tracker_without_order_number():
    """Tracker without order number slot."""
    return Tracker(
        sender_id="test_user",
        slots={"order_no_value": None},
        latest_message={"intent": {"name": "order_number"}},
        events=[],
        paused=False,
        followup_action=None,
        active_loop=None,
        latest_action_name="action_listen"
    )

"""
Testing functions related to getting category name 
"""
@pytest.fixture
def tracker_with_product_category_name():
    """Tracker with a pre-filled product category name slot."""
    return Tracker(
        sender_id="test_user",
        slots={"product_category": "laptop"},
        latest_message={"intent": {"name": "search_product"}},
        events=[],
        paused=False,
        followup_action=None,
        active_loop=None,
        latest_action_name="action_listen"
    )

@pytest.fixture
def tracker_without_product_category_name():
    """Tracker without product category name slot."""
    return Tracker(
        sender_id="test_user",
        slots={"product_category": None},
        latest_message={"intent": {"name": "search_product"}},
        events=[],
        paused=False,
        followup_action=None,
        active_loop=None,
        latest_action_name="action_listen"
    )

"""
Testing functions related to getting all category data
"""
@pytest.fixture
def tracker_with_product_category_name_say_category_data():
    """Tracker with a pre-filled product category name slot."""
    return Tracker(
        sender_id="test_user",
        slots={"product_category": "Table"},
        latest_message={"intent": {"name": "affirm"}},
        events=[],
        paused=False,
        followup_action=None,
        active_loop=None,
        latest_action_name="action_listen"
    )

@pytest.fixture
def tracker_without_product_category_name_say_category_data():
    """Tracker without product category name slot."""
    return Tracker(
        sender_id="test_user",
        slots={"product_category": None},
        latest_message={"intent": {"name": "affirm"}},
        events=[],
        paused=False,
        followup_action=None,
        active_loop=None,
        latest_action_name="action_listen"
    )

@pytest.fixture
def domain():
    """Domain dictionary fixture."""
    return {"responses": {}}

"""
Testing and executing functions related to ordering 
"""
@pytest.mark.asyncio
async def test_action_fetch_order_status_with_order_number(dispatcher, tracker_with_order_number, domain):
    action = ActionSayOrderStatus()
    events = await action.run(dispatcher, tracker_with_order_number, domain)

    assert len(events) == 0
    messages = [message["text"] for message in dispatcher.messages]
    assert "Your order is currently pending confirmation. It will be dispatched after confirmation." in messages


@pytest.mark.asyncio
async def test_action_fetch_order_status_without_order_number(dispatcher, tracker_without_order_number, domain):
    action = ActionSayOrderStatus()
    events = await action.run(dispatcher, tracker_without_order_number, domain)

    assert len(events) == 1  # Expect 1 event
    assert events[0]["event"] == "slot"
    assert events[0]["name"] == "order_no_value"
    assert events[0]["value"] is None

    messages = [message["text"] for message in dispatcher.messages]
    assert "Sorry, your order number is invalid. Please provide a valid order number." in messages

"""
Testing and executing functions related to getting category name 
"""
@pytest.mark.asyncio
async def test_action_confirm_product_name_with_product_category_name(dispatcher, tracker_with_product_category_name, domain):
    action = ActionSayProductInquiry()
    events = await action.run(dispatcher, tracker_with_product_category_name, domain)

    assert len(events) == 0
    messages = [message["text"] for message in dispatcher.messages]
    assert "Did you mean 'Laptops'?" in messages


@pytest.mark.asyncio
async def test_action_confirm_product_name_without_product_category_name(dispatcher, tracker_without_product_category_name, domain):
    action = ActionSayProductInquiry()
    events = await action.run(dispatcher, tracker_without_product_category_name, domain)

    assert len(events) == 0

    messages = [message["text"] for message in dispatcher.messages]
    assert "Sorry, could you specify what you are looking for again !" in messages

"""
Testing and executing functions related to getting all category data
"""
@pytest.mark.asyncio
async def test_action_fetch_category_data_with_product_category_name(dispatcher, tracker_with_product_category_name_say_category_data, domain):
    action = ActionSayCategoryData()
    events = await action.run(dispatcher, tracker_with_product_category_name_say_category_data, domain)

    # Validate the number of events
    assert len(events) == 1  # Expecting exactly 1 event
    event = events[0]

    # Validate the event details
    assert event["event"] == "slot"
    assert event["name"] == "user_product_data"
    assert event["value"] is not None
    assert isinstance(event["value"], list)  # Ensure the value is a list

    # Validate the content of the event value (example fields)
    first_item = event["value"][0]
    assert first_item["category"] == "Table"
    assert first_item["description"] == "Test"
    assert first_item["name"] == "Test"
    assert first_item["price"] == 9999.99


@pytest.mark.asyncio
async def test_action_fetch_category_data_without_product_category_name(dispatcher, tracker_without_product_category_name_say_category_data, domain):
    action = ActionSayCategoryData()
    events = await action.run(dispatcher, tracker_without_product_category_name_say_category_data, domain)

    assert len(events) == 0

    messages = [message["text"] for message in dispatcher.messages]
    assert "Sorry, could you specify what you are looking for again !" in messages