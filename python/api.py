import requests
import random
import json

url = "https://bottesting2.saarthi.ai/webhook_manappuram/webhook"


def request_1(session_id,message=None,intent=None):
    payload = json.dumps({
        "user_id" : "8660373334",
        "request_id" : "request111130",
        "sender" : session_id,
        "message" :  message,
        "nlu_data":{
        "label": [
            {
                "name": intent,
                "confidence": "1.0"
            },
            {
                "name": "agree_to_proceed",
                "confidence": "0.0008543797"
            },
            {
                "name": "greet",
                "confidence": "0.00031966175"
            }
        ]
    },
        "ner_data":[
            {
            "entity":"date",
            "extractor":"saarthi-ner",
            "value":"04/12/2022"
    }]
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    print(response["data"])

request_1(2,message="/initial_message",intent="/initial_message")
request_1(2,message="no",intent="deny")
request_1(2,message="agree_to_pay",intent="agree_to_pay")