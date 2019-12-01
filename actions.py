# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


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
#         dispatcher.utter_message("Hello World!")
#
#         return []

# from __future__ import absolute_import
# from __future__ import division
# from __future__ import unicode_literals
import requests
import json

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionCheckLeave(Action):
    def name(self):
        return "action_check_leave"

    def run(self, dispatcher, tracker, domain):
        emp = tracker.get_slot('employee_name')
        print(emp)
        #print(tracker.text)
        #params = {
        #  'access_key': 'AccessKey',
        #  'query': emp
        #}
        #api_result = requests.get('URL', params)
        #print(api_result.text)
        #dispatcher.utter_message(api_result)
        #api_response = api_result.json()
        #print(api_response)
        response = "Employee has 32 leaves"
        dispatcher.utter_message(response)
        return []

