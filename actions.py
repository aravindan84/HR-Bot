
import requests
import json

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionCheckLeave(Action):
    def name(self):
        return "action_check_leave"

    def run(self, dispatcher, tracker, domain):
        emp = tracker.get_slot('emp_name')
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
