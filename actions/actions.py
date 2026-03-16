# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action,Tracker

# Action to provide medicine information
class ActionProvideMedicineInfo(Action):
    def name(self) -> str:
        return "action_provide_medicine_info"

    def run(self, dispatcher, tracker, domain):
        medicine_name = tracker.get_slot("medicine_name")

        # Example response for medicine info
        if medicine_name:
            response = f"{medicine_name} is commonly used for treating pain, fever, or related conditions."
        else:
            response = "Here is the information about common medicines: Melatonin for sleep, Diphenhydramine for allergies, and Ibuprofen for pain relief."

        dispatcher.utter_message(text=response)
        return []


# Action to check inventory
class ActionCheckInventory(Action):
    def name(self) -> str:
        return "action_check_inventory"

    def run(self, dispatcher, tracker, domain):
        medicine_name = tracker.get_slot("medicine_name")

        # Example inventory data
        inventory = {
            "Paracetamol": 20,
            "Ibuprofen": 10,
            "Aspirin": 0,
        }

        if medicine_name in inventory:
            quantity = inventory[medicine_name]
            if quantity > 0:
                dispatcher.utter_message(text=f"{medicine_name} is in stock with {quantity} units.")
            else:
                dispatcher.utter_message(text=f"Sorry, {medicine_name} is currently out of stock.")
        else:
            dispatcher.utter_message(text=f"Sorry, {medicine_name} is not in our inventory.")

        return []


# Action to provide price information
class ActionProvidePrice(Action):
    def name(self) -> str:
        return "action_provide_price"

    def run(self, dispatcher, tracker, domain):
        medicine_name = tracker.get_slot("medicine_name")

        # Example pricing datarasa shell

        pricing = {
            "Paracetamol": 5.00,
            "Ibuprofen": 10.00,
            "Aspirin": 7.50,
        }

        if medicine_name in pricing:
            price = pricing[medicine_name]
            dispatcher.utter_message(text=f"The price of {medicine_name} is ${price:.2f}.")
        else:
            dispatcher.utter_message(text=f"Sorry, I don't have pricing information for {medicine_name}.")

        return []


# Action to provide side effect information
class ActionProvideSideEffects(Action):
    def name(self) -> str:
        return "action_provide_side_effects"

    def run(self, dispatcher, tracker, domain):
        medicine_name = tracker.get_slot("medicine_name")

        # Example side effects data
        side_effects = {
            "Paracetamol": "Side effects include nausea, rash, and headache.",
            "Ibuprofen": "Side effects include stomach upset, dizziness, and rash.",
            "Aspirin": "Side effects include stomach bleeding, heartburn, and nausea.",
        }

        if medicine_name in side_effects:
            dispatcher.utter_message(text=f"Side effects of {medicine_name}: {side_effects[medicine_name]}")
        else:
            dispatcher.utter_message(text=f"Sorry, I don't have side effect information for {medicine_name}.")

        return []


# Action to provide generic medicine alternatives
class ActionProvideGenericOption(Action):
    def name(self) -> str:
        return "action_provide_generic_option"

    def run(self, dispatcher, tracker, domain):
        medicine_name = tracker.get_slot("medicine_name")

        # Example generic medicine data
        generic_options = {
            "Paracetamol": "Acetaminophen",
            "Ibuprofen": "Generic Ibuprofen",
            "Aspirin": "Acetylsalicylic Acid",
        }

        if medicine_name in generic_options:
            dispatcher.utter_message(text=f"A generic alternative to {medicine_name} is {generic_options[medicine_name]}.")
        else:
            dispatcher.utter_message(text=f"Sorry, I don't have generic alternatives for {medicine_name}.")

        return []


# Action to provide expiry information
class ActionProvideExpiry(Action):
    def name(self) -> str:
        return "action_provide_expiry"

    def run(self, dispatcher, tracker, domain):
        medicine_name = tracker.get_slot("medicine_name")

        # Example expiry data
        expiry_dates = {
            "Paracetamol": "2025-12-31",
            "Ibuprofen": "2024-06-30",
            "Aspirin": "2023-09-15",
        }

        if medicine_name in expiry_dates:
            dispatcher.utter_message(text=f"The expiry date of {medicine_name} is {expiry_dates[medicine_name]}.")
        else:
            dispatcher.utter_message(text=f"Sorry, I don't have expiry information for {medicine_name}.")

        return []


# Action to ask user for prescription
class ActionRequestPrescription(Action):
    def name(self) -> str:
        return "action_request_prescription"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Please upload your prescription to proceed with this request.")
        return []