import json
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

date = (datetime.now() + timedelta(hours=7)).strftime('%Y-%m-%d %H:%M')
# test room
webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAtPL3b4M/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=foKsGYG0AliLLJX6hK6rk6qg9k2VedIpgIvq3Tz-Dp0%3D'
# official room
# webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAyuJim_I/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=sg8w7dXX3wcccZX5zKATXoL3ZcI787YLj6yTSfvf-oE%3D'
# send result to chat room via google webhook
def send_google_chat(message, app_name, environment):
    url = webhook_url
    data = f"`{date}` `{environment}` *{app_name}* is not running"
    bot_message = {'text': data}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    byte_encoded = json.dumps(bot_message).encode('utf-8')
    req = urllib.request.Request(url=url, data=byte_encoded, headers=message_headers)
    response = urllib.request.urlopen(req)

