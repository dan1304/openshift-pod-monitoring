import time
from PodDataCollect import *
from GoogleChat import *
import logging, os
from dotenv import load_dotenv

# load vars from .env config file
load_dotenv(".env")
chat_room = os.getenv('CHAT_ROOM')
IDLE_TIME = int(os.getenv('IDLE_TIME'))

class PodStatusCheck:
    def __init__(self, app_list_file, environment):
        self.app_list_file = app_list_file
        self.environment = environment

    def check_app_status(self):
        app_list = []
        with open(self.app_list_file, 'r') as f:
            for line in f:
                app = line.split()
                app_list.append(app)
                logging.info(f"Apps list: {app_list}")
        while True:
            # try:
            for app in app_list:
                app_name = app[0]
                logging.info(f"App to check: {app_name} ")
                pod_info = PodDataCollect(app_name, 0, self.environment)
                shell_cmd = pod_info.shell_cmd()
                logging.info(f"CMD to run: {shell_cmd}")
                pod_status = pod_info.get_pods(shell_cmd)
                if 'true' not in str(pod_status):
                    pod_info.increase_count()
                    failed_count = pod_info.get_failed_count()
                    if failed_count[0] >= 3:
                        failed_mins = failed_count[0]*IDLE_TIME/60
                        alert = GoogleChat(pod_status, app_name, self.environment, failed_mins, chat_room)
                        logging.info("Sending alert to Google Chat")
                        alert.send_google_chat()
                else:
                    pod_info.reset_count()
            logging.info(f"Idle for {IDLE_TIME}s before continuing checking {self.environment}...")
            time.sleep(IDLE_TIME)
            # except AttributeError as e:
            #   logging.info("Check params:" + str(e))
            # except:
            #     logging.info("Something wrong!")

