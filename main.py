import time
from flask import Flask
from multiprocessing import Process, Value
import googlechat
from podStatus import podStatus
import logging
import sqlite3

# import ipdb

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

gg_msg = ''
nested_app_list = {
					'mms-api-gateway': {'failed_count': 0},
					'mms-centralize-config': {'failed_count': 0}
                }
#ipdb.set_trace()


for app_name, failed_count in  nested_app_list.items():
    print(app_name, failed_count)

@app.route('/pods', methods=['GET'])
def pod_alert(loop_on):
    for app_name, failed_count in nested_app_list.items():
        print(app_name)
        app1 = podStatus(app_name, failed_count)
        while True:
            gg_msg = app1.get_pods()
            print(type(gg_msg))
            if 'true' not in str(gg_msg):
                googlechat.send_google_chat(gg_msg)
            else:
                pass
            time.sleep(260)
    
if __name__ == "__main__":
    recording_on = Value('b', True)
    p = Process(target=pod_alert, args=(recording_on,))
    p.start()  
    app.run(debug=True, use_reloader=False)
    p.join()

       
