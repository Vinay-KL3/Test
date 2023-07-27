import requests
import random
import json
import pandas as pd
import csv
import openpyxl
import xlsxwriter

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
    #print(f'input message is {message} bot output is ------>{response["data"][0]["text"]}'+"\n")
    print(f'{response["data"][0]["text"]}'+"\n")
    #print(C)




session_id = random.randint(1,100000000)

print(session_id)




with open('/Users/vinay_kl/Downloads/demo3.csv', 'r') as f:
    reader = csv.reader(f)
    the_whole_file = list(reader)    
    
    
count = 0
while (count < 17):
    count = count + 1
    
     message = the_whole_file[count][1]
     
     request_1(session_id,message)

