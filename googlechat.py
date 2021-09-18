import json
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

class GoogleChat:
    def __init__(self, message, app_name, environment, failed_time, chat_room):
        self.message = message
        self.app_name = app_name
        self.environment = environment
        self.failed_time = failed_time
        self.chat_room = chat_room
    
    def send_google_chat(self):
        date = (datetime.now() + timedelta(hours=7)).strftime('%Y-%m-%d %H:%M')
        data = f"`{date}` `{self.environment}` *{self.app_name}* not running for {self.failed_time} mins"
        bot_message = {'text': data}
        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        byte_encoded = json.dumps(bot_message).encode('utf-8')
        req = urllib.request.Request(url=self.chat_room, data=byte_encoded, headers=message_headers)
        response = urllib.request.urlopen(req)

