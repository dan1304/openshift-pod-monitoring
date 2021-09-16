import subprocess, time
import googlechat
from PodDataCollect import *
IDLE_TIME = 300
class PodStatusCheck:

    def __init__(self, app_list_file, environment):
        self.app_list_file = app_list_file
        self.environemnt = environment

    def check_app_status(self):
        app_list = []
        with open(self.app_list_file, 'r') as f:
            for line in f:
                app = line.split()
                app_list.append(app)
                print(app_list)
        while True:
            try:
                for app in app_list:
                    app_name = app[0]
                    print(f"App to check: {app_name} ")
                    pod_info = PodDataCollect(app_name, 0, self.environemnt)
                    shell_cmd = pod_info.shell_cmd()
                    print(shell_cmd)
                    pod_status = pod_info.get_pods(shell_cmd)
                    if 'true' not in str(pod_status):
                        pod_info.increase_count()
                        failed_count = pod_info.get_failed_count()
                        if failed_count[0] >= 3:
                            # failed_time = failed_count[0]*IDLE_TIME
                            googlechat.send_google_chat(pod_status, app_name, self.environemnt)
                    else:
                        pod_info.reset_count()
                print(f"Idle for {IDLE_TIME}s before continuing ...")
                time.sleep(IDLE_TIME)
            except AttributeError:
                print("Check param if not passed...")
            except:
                print("Something wrong!")