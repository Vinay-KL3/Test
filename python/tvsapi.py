import requests
import random
import json

url = "https://poojafin.saarthi.ai/lead_english/webhook"


def request_1(session_id,message=None,intent=None):
    payload = json.dumps({
    "user_id" : "7893893270",
    "request_id" : "request1127",
    "sender" : session_id,
    "message" :  message
})
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    print(f'input message is {message} bot output is ------>{response["data"][0]["text"]}'+"\n")


session_id = random.randint(1,100)
request_1(session_id,message="/initial_message")
request_1(session_id,message="yes")
request_1(session_id,message="yes")
