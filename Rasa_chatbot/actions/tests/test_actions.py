# import pytest
# from rasa_sdk import Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict
# from ..actions import ActionSayOrderStatus
#
# @pytest.fixture
# def dispatcher():
#     """Fixture for creating a dispatcher instance."""
#     return CollectingDispatcher()
#
# @pytest.fixture
# def tracker_with_order_number():
#     """Tracker with a pre-filled order number slot."""
#     return Tracker(
#         sender_id="test_user",
#         slots={"order_no_value": "1122334455"},
#         latest_message={"intent": {"name": "order_number"}},
#         events=[],
#         paused=False,
#         followup_action=None,
#         active_loop=None
#     )
#
# @pytest.fixture
# def tracker_without_order_number():
#     """Tracker without order number slot."""
#     return Tracker(
#         sender_id="test_user",
#         slots={"order_no_value": None},
#         latest_message={"intent": {"name": "order_number"}},
#         events=[],
#         paused=False,
#         followup_action=None,
#         active_loop=None
#     )
#
# @pytest.fixture
# def domain():
#     """Domain dictionary fixture."""
#     return {"responses": {}}
#
# def test_action_fetch_order_status_with_order_number(dispatcher, tracker_with_order_number, domain):
#     action = ActionSayOrderStatus()
#     events = action.run(dispatcher, tracker_with_order_number, domain)
#
#     assert len(events) == 0
#     messages = [message["text"] for message in dispatcher.messages]
#     assert "Your order is currently pending confirmation. It will be dispatched after confirmation." in messages
#
# def test_action_fetch_order_status_without_order_number(dispatcher, tracker_without_order_number, domain):
#     action = ActionSayOrderStatus()
#     events = action.run(dispatcher, tracker_without_order_number, domain)
#
#     assert len(events) == 0
#     messages = [message["text"] for message in dispatcher.messages]
#     assert "Sorry, your order number is invalid. Please provide a valid order number." in messages


# import pytest
# from rasa_sdk import Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict
# from ..actions import ActionSayOrderStatus
#
# @pytest.fixture
# def dispatcher():
#     """Fixture for creating a dispatcher instance."""
#     return CollectingDispatcher()
#
# @pytest.fixture
# def tracker_with_order_number():
#     """Tracker with a pre-filled order number slot."""
#     return Tracker(
#         sender_id="test_user",
#         slots={"order_no_value": "1122334455"},
#         latest_message={"intent": {"name": "order_number"}},
#         events=[],
#         paused=False,
#         followup_action=None,
#         active_loop=None,
#         latest_action_name="action_listen"  # Added required argument
#     )
#
# @pytest.fixture
# def tracker_without_order_number():
#     """Tracker without order number slot."""
#     return Tracker(
#         sender_id="test_user",
#         slots={"order_no_value": None},
#         latest_message={"intent": {"name": "order_number"}},
#         events=[],
#         paused=False,
#         followup_action=None,
#         active_loop=None,
#         latest_action_name="action_listen"  # Added required argument
#     )
#
# @pytest.fixture
# def domain():
#     """Domain dictionary fixture."""
#     return {"responses": {}}
#
# def test_action_fetch_order_status_with_order_number(dispatcher, tracker_with_order_number, domain):
#     action = ActionSayOrderStatus()
#     events = action.run(dispatcher, tracker_with_order_number, domain)
#
#     assert len(events) == 0
#     messages = [message["text"] for message in dispatcher.messages]
#     assert "Your order is currently pending confirmation. It will be dispatched after confirmation." in messages
#
# def test_action_fetch_order_status_without_order_number(dispatcher, tracker_without_order_number, domain):
#     action = ActionSayOrderStatus()
#     events = action.run(dispatcher, tracker_without_order_number, domain)
#
#     assert len(events) == 0
#     messages = [message["text"] for message in dispatcher.messages]
#     assert "Sorry, your order number is invalid. Please provide a valid order number." in messages

import pytest
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from ..actions import ActionSayOrderStatus
from ..actions import ActionSayProductInquiry
from ..actions import ActionSayCategoryData
from ..actions import ActionConfirmProduct

@pytest.fixture
def dispatcher():
    """Fixture for creating a dispatcher instance."""
    return CollectingDispatcher()

#ORDER--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#PRODUCT_INQUIRY----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#CATEGORY_DATA----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#CONFIRM_PRODUCT----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@pytest.fixture
def tracker_with_item_no_user_product_data():
    """Tracker with a pre-filled product category name slot."""
    return Tracker(
        sender_id="test_user",
        slots={"item_no": "1", "user_product_data": "[{'product_id': 999, 'category': 'Table', 'description': 'Test', 'name': 'Test', 'price': 9999.99, 'quantity': 1, 'rating': 5.0, 'status': 'in_stock'}]"},
        latest_message={"intent": {"name": "buy_product"}},
        events=[],
        paused=False,
        followup_action=None,
        active_loop=None,
        latest_action_name="action_listen"
    )

@pytest.fixture
def tracker_without_item_no_user_product_data():
    """Tracker without product category name slot."""
    return Tracker(
        sender_id="test_user",
        slots={"item_no": None, "user_product_data": None},
        latest_message={"intent": {"name": "buy_product"}},
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

#ORDER--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#PRODUCT_INQUIRY----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#CATEGORY_DATA----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

    # messages = [message["text"] for message in dispatcher.messages]
    #
    # # Validate the content of the messages
    # assert len(messages) == 3  # Expecting exactly 3 messages
    # assert "These are all the products we have in Table category." in messages[0]  # Check the content of the first message
    # assert "1. Name: Test Description: Test Price: 9999.99" in messages[1]  # Check the content of the second message
    # assert "Please use the index number when referring to the item you are interested in." in messages[2]  # Check the content of the third message


@pytest.mark.asyncio
async def test_action_fetch_category_data_without_product_category_name(dispatcher, tracker_without_product_category_name_say_category_data, domain):
    action = ActionSayCategoryData()
    events = await action.run(dispatcher, tracker_without_product_category_name_say_category_data, domain)

    assert len(events) == 0

    messages = [message["text"] for message in dispatcher.messages]
    assert "Sorry, could you specify what you are looking for again !" in messages

#CONFIRM_PRODUCT----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# @pytest.mark.asyncio
# async def test_action_confirm_product_with_item_no_user_product_data(dispatcher, tracker_with_item_no_user_product_data, domain):
#     action = ActionConfirmProduct()
#     events = await action.run(dispatcher, tracker_with_item_no_user_product_data, domain)

    # assert len(events) == 0
    # messages = [message["text"] for message in dispatcher.messages]
    # assert "Did you mean Test. Would you like to add place this order" in messages

    # Validate the events
    # assert len(events) == 1  # Update to reflect the actual number of events
    # assert events[1]["event"] == "slot"
    # assert events[1]["name"] == "item_no"
    # assert events[1]["value"] is None

    # # Validate the dispatched messages
    # messages = [message["text"] for message in dispatcher.messages]
    #
    # # Check the number of messages
    # assert len(messages) == 1  # Adjust if multiple messages are expected
    #
    # # Validate message content
    # expected_message = "Did you mean Test. Would you like to place this order?"
    # assert expected_message in messages[0]  # Adjust for exact or partial match


# @pytest.mark.asyncio
# async def test_action_confirm_product_without_item_no_user_product_data(dispatcher, tracker_without_item_no_user_product_data, domain):
#     action = ActionConfirmProduct()
#     events = await action.run(dispatcher, tracker_without_item_no_user_product_data, domain)
#
#     assert len(events) == 0
#
#     messages = [message["text"] for message in dispatcher.messages]
#     assert "Your item number is invalid !" in messages