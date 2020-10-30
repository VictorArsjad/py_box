import json
import requests

import credentials


def send_message(text):
    endpoint = "https://messages-sandbox.nexmo.com/v0.1/messages"
    payload = {"from": {"type": "whatsapp", "number": credentials.nexmo_number},
               "to": {"type": "whatsapp", "number": credentials.wa_number},
               "message": {"content": {"type": "text", "text": text}}}
    headers = {'Content-Type': "application/json", 'Accept': "application/json"}
    r = requests.post(url=endpoint,
                      auth=(credentials.user, credentials.pwd),
                      headers=headers,
                      data=json.dumps(payload))

    if r.status_code == requests.codes.accepted:
        print("message sent successfully with UUID ", r.json()['message_uuid'])
    else:
        print(r.raise_for_status())


send_message("It's working! Woohoo!")
