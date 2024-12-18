# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import httpx  # Async HTTP client for requests
from rapidfuzz import process
import ast

class ActionSayOrderStatus(Action):
    """
    Function is used to check order status
    """
    def name(self) -> Text:
        return "action_say_order_status"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Retrieve the order number from the slot
        order_number = tracker.get_slot("order_no_value")

        # Order number validation
        if (not order_number or int(len(order_number)) < 10
                or int(len(order_number)) >= 12
                or not order_number.isdigit()):
            dispatcher.utter_message(
                text="Sorry, your order number is invalid. Please provide a valid order number."
            )
            return [SlotSet("order_no_value", None)]

        url = "http://127.0.0.1:8000/value/"

        try:
            # Make an asynchronous POST request to the FastAPI server
            async with httpx.AsyncClient() as client:
                response = await client.post(url,
                                             json={"order_id": order_number}) #, timeout=10.0
                response.raise_for_status()  # Raise an error for 4xx/5xx responses
                # print(f"ordered {response.json()}")

            # Parse the JSON response from FastAPI
            item = response.json()
            item_status = item.get("status")

            # Craft response based on the item's status
            if item_status == "pending":
                dispatcher.utter_message(
                    text=f"Your order is currently pending confirmation. It will be dispatched after confirmation."
                )
            elif item_status == "transit":
                dispatcher.utter_message(
                    text=f"Your order is in transit and should arrive within 24 hours."
                )
            elif item_status == "delivered":
                dispatcher.utter_message(
                    text=f"Your order has been delivered. Thank you for shopping with us!"
                )
            else:
                dispatcher.utter_message(
                    text=f"Your order status is: {item_status}. Please contact support for more details."
                )

        except httpx.RequestError as e:
            # Handle connection issues
            dispatcher.utter_message(
                text="There was a network error while retrieving your order. Please try again later."
            )
            # print(f"Network error: {str(e)}")

        except httpx.HTTPStatusError as e:
            # Handle HTTP errors
            dispatcher.utter_message(
                text=f"Unable to retrieve order information (HTTP {e.response.status_code}). Please try again later."
            )
            # print(f"HTTP error: {e.response.status_code} - {e.response.text}")

        return []


class ActionSayProductInquiry(Action):
    """
    Function is used to confirm product name
    """
    def name(self) -> Text:
        return "action_say_product_inquiry"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_category_name = tracker.get_slot("product_category")

        if not product_category_name :
            dispatcher.utter_message(
                text="Sorry, could you specify what you are looking for again !"
            )
            return []

        url = "http://127.0.0.1:8000/sort/"
        # print(f"product category name is : {product_category_name}")

        try:
            # Make an asynchronous POST request to the FastAPI server
            async with httpx.AsyncClient() as client:
                response = await client.post(url)  # , timeout=10.0
                response.raise_for_status()  # Raise an error for 4xx/5xx responses
                # print(f"THis is the responce: {response.json()}")


            # Parse the list response from FastAPI
            items = response.json()

            # Fuzzy match user input with product names
            match, score, index = process.extractOne(product_category_name, items)
            # print(f"Match: {match}, Score: {score}, Index: {index}")

            if score > 70:  # Threshold for a good match
                dispatcher.utter_message(
                    text=f"Did you mean '{match}'?"
                )
            else:
                dispatcher.utter_message(
                    text="Sorry, I couldn't find anything matching your query."
                )

        except httpx.RequestError as e:
            # Handle connection issues
            dispatcher.utter_message(
                text="There was a network error while retrieving your product category. Please try again later."
            )
            # print(f"Network error: {str(e)}")

        except httpx.HTTPStatusError as e:
            # Handle HTTP errors
            dispatcher.utter_message(
                text=f"Unable to retrieve order information (HTTP {e.response.status_code}). Please try again later."
            )
            # print(f"HTTP error: {e.response.status_code} - {e.response.text}")

        return []

class ActionSayCategoryData(Action):
    """
    Function is used to get all the data related to a category
    """
    def name(self) -> Text:
        return "action_say_category_data"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Globalizing the category name
        global category

        product_category_name = tracker.get_slot("product_category")

        if not product_category_name:
            dispatcher.utter_message(
                text="Sorry, could you specify what you are looking for again !"
            )
            return []

        try:
            # Make an asynchronous POST request to the FastAPI server
            async with httpx.AsyncClient() as client:
                response = await client.post("http://127.0.0.1:8000/sort/")  # , timeout=10.0
                response.raise_for_status()  # Raise an error for 4xx/5xx responses
                # print(f"THis is the responce: {response.json()}")


            # Parse the list response from FastAPI
            items = response.json()

            # Fuzzy match user input with product names
            match, score, index = process.extractOne(product_category_name, items)
            # print(f"Match: {match}, Score: {score}, Index: {index}")

            if score > 70:  # Threshold for a good match
                category = match
            else:
                dispatcher.utter_message(
                    text="wrong path"
                )

        except httpx.RequestError as e:
            # Handle connection issues
            dispatcher.utter_message(
                text="There was a network error while retrieving your product category. Please try again later."
            )
            # print(f"Network error: {str(e)}")

        except httpx.HTTPStatusError as e:
            # Handle HTTP errors
            dispatcher.utter_message(
                text=f"Unable to retrieve order information (HTTP {e.response.status_code}). Please try again later."
            )
            # print(f"HTTP error: {e.response.status_code} - {e.response.text}")

        try:
            # Make an asynchronous POST request to the FastAPI server
            async with httpx.AsyncClient() as client:
                response = await client.post("http://127.0.0.1:8000/category/", json={"category": category})  # , timeout=10.0
                response.raise_for_status()  # Raise an error for 4xx/5xx responses
                # print(f"THis is the response: {response}")
                # print(f"THis is the response json: {response.json()}")

            all_products = response.json()

            # print(f"Loop works {all_products}")

            if not all_products:
                dispatcher.utter_message(
                    text="Oops something went wrong !"
                )
                return []

            dispatcher.utter_message(
                text=f"These are all the products we have in {category} category."
            )
            # print("Loop works")
            x = 1
            for product in all_products:
                # print("in loop")
                dispatcher.utter_message(
                    text=f"{x}. Name: {product['name']} \n  Description: {product['description']} \n  Price: {product['price']} \t"
                )
                x = x+1

            dispatcher.utter_message(
                text="Please use the index number when referring to the item you are interested in."
            )
            return [SlotSet("user_product_data", all_products)]

        except httpx.RequestError as e:
            # Handle connection issues
            dispatcher.utter_message(
                text="There was a network error while retrieving your product category. Please try again later."
            )
            # print(f"Network error: {str(e)}")

        except httpx.HTTPStatusError as e:
            # Handle HTTP errors
            dispatcher.utter_message(
                text=f"Unable to retrieve order information (HTTP {e.response.status_code}). Please try again later."
            )
            # print(f"HTTP error: {e.response.status_code} - {e.response.text}")

        return []

class ActionConfirmProduct(Action):
    """
    Function is used to confirm the index number when referring to the product
    """
    def name(self) -> Text:
        return "action_confirm_product"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        item_no = tracker.get_slot("item_no")
        # print(item_no)
        # print(type(item_no), item_no)

        if not item_no or int(len(item_no)) > 2:
            dispatcher.utter_message(
                text="Your item number is invalid !"
            )
            return [SlotSet("item_no", None)]

        user_product_data = tracker.get_slot("user_product_data")

        def convert_to_dict(value):
            if isinstance(value, str):  # Check if the value is a string
                try:
                    # Attempt to convert the string to a dictionary
                    return ast.literal_eval(value)
                except (ValueError, SyntaxError):
                    # Return the original value if conversion fails
                    return value
            return value

        converted = convert_to_dict(user_product_data)

        if not user_product_data:
            dispatcher.utter_message(
                text="Data unavailable"
            )
            return []

        dispatcher.utter_message(
            text=f"Did you mean {converted[int(item_no)-1]['name']}. \n Would you like to add place this order"
        )

        return []

class ActionAskChatGPT(Action):
    """
    Function is used to get gpt response
    """
    def name(self) -> Text:
        return "action_ask_chatgpt"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        item_no = tracker.get_slot("item_no")

        user_product_data = tracker.get_slot("user_product_data")

        message = f"Could you give me more information on {user_product_data[int(item_no)-1]['name']}"


        async with httpx.AsyncClient() as client:
            try:
                # Send user message to FastAPI server
                response = await client.post(
                    "http://127.0.0.1:8000/gpt/",
                    json={"message": message}, timeout=10.0)

                # Check for successful response
                if response.status_code == 200:
                    result = response.json()
                    chatgpt_response = result.get("response", "Sorry, no response available.")
                else:
                    chatgpt_response = "Sorry, I couldn't process your request."

                final_res = f"{chatgpt_response} \nWOULD YOU LIKE TO BUY THIS PRODUCT !"

                # Send response back to RASA
                dispatcher.utter_message(
                    text=final_res
                )

            except httpx.RequestError as exc:
                dispatcher.utter_message(
                    text="Sorry, I couldn't process your request."
                )
                # print(f"An error occurred while requesting {exc.request.url!r}: {exc}")

        return []
