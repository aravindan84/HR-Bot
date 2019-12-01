
## story 002
* greet
  - utter_greet
* inform
  - utter_ask_employee_name
  - slot{"employee_name": "jack"}
* inform{"employee_name": "jack"}
  - slot{"employee_name": "jack"}
  - action_check_leave
  - slot{"employee_name": "jack"}
* goodbye
  - utter_goodbye
  - export

## New Story

* greet
    - utter_greet
* inform
    - utter_ask_employee_name
    - slot{"employee_name": "jack"}
* inform{"employee_name": "jack"}
  - slot{"employee_name": "jack"}
  - action_check_leave
  - slot{"employee_name": "jack"}
