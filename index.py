import json
import requests

def send_message(url, headers, message):
  data = {'text': message}
  requests.post(url, headers=headers, data=json.dumps(data))

swit_url = "https://hook.swit.io/chat/" #chat_channel_url
headers = {"Content-Type":"application/json; chartset-utf-8"}

message = "hello world!" #message_here

if __name__=="__main__":
  send_message(swit_url, headers, message)