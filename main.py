import time
from flask import Flask
from multiprocessing import Process, Value
import googlechat
from podStatus import *
import logging

# import ipdb

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

gg_msg = ''
nested_app_list = {
					'mms-api-gateway': {'failed_count': 0},
					'mms-centralize-config': {'failed_count': 0}
                }
for app_name, failed_count in  nested_app_list.items():
    print(app_name, failed_count)

@app.route('/pods', methods=['GET'])
def pod_alert(loop_on):
    while True:
        try:
            for app_name, failed_count in nested_app_list.items():
                print(app_name)
                pod_status = podStatus(app_name, failed_count)
                shell_cmd = pod_status.shell_cmd()
                print(shell_cmd)
                gg_msg = pod_status.get_pods(shell_cmd)
                print(type(gg_msg))
                if 'true' not in str(gg_msg):
                    pod_status.increase_count()
                    failed_count = pod_status.get_failed_count()
                    if failed_count[0] >= 3:
                        googlechat.send_google_chat(gg_msg)
                else:
                    pod_status.reset_count()
            time.sleep(300)
        except:
            print("Something wrong?")
    
if __name__ == "__main__":
    recording_on = Value('b', True)
    p = Process(target=pod_alert, args=(recording_on,))
    p.start()  
    app.run(debug=True, use_reloader=False)
    p.join()

       
