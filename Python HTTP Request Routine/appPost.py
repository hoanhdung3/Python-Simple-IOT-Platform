#This routine for sending IoT data sensor to server

import requests
import json
import time

security_code = "123"
id_hardware = 2

#Infinite looping (ctrl + C to stop the worker)
while True:
    #URL of the api
    url = "http://127.0.0.1:5000/addhardwarelog"
    body = {
        "id_hardware":2,
        "security_code":security_code,
        "ph_level":15,
        "temperature":17,
        "humidity":23,
        "water_level":27,
        #Image must be a base64 or blob format
        "image":"4"
    }
    response = requests.post(url, json=body)
    responsejson = json.loads(response.text)
    print(responsejson["message"])
    #sleep 5 second
    time.sleep(5)
    continue