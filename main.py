from flask import Flask
from multiprocessing import Process, Value
from PodDataCollect import *
from PodStatusCheck import *
import logging
import ipdb

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

gg_msg = ''
app_list_file = "app_list_to_check.txt"

@app.route('/staging', methods=['GET'])
def pod_alert_staging(loop_on):
    staging_pods = PodStatusCheck(app_list_file, "equator-default-staging")
    staging_pods.check_app_status()

@app.route('/dev', methods=['GET'])
def pod_alert_dev(loop_on):
    dev_pods = PodStatusCheck(app_list_file, "equator-default-dev")
    dev_pods.check_app_status()    

@app.route('/release1', methods=['GET'])
def pod_alert_release1(loop_on):
    release1_pods = PodStatusCheck(app_list_file, "equator-default-release1")
    release1_pods.check_app_status() 

@app.route('/release2', methods=['GET'])
def pod_alert_release2(loop_on):
    release2_pods = PodStatusCheck(app_list_file, "equator-default-release2")
    release2_pods.check_app_status()    

@app.route('/performance', methods=['GET'])
def pod_alert_performance(loop_on):
    performance_pods = PodStatusCheck(app_list_file, "equator-default-performance")
    performance_pods.check_app_status()    

if __name__ == "__main__":
    recording_on = Value('b', True)
    # for env in ("equator-default-dev", "equator-default-release1", "equator-default-release2", "equator-default-staging" ):
    p1 = Process(target=pod_alert_staging, args=(recording_on,))
    p2 = Process(target=pod_alert_dev, args=(recording_on,))
    p3 = Process(target=pod_alert_release1, args=(recording_on,))
    p4 = Process(target=pod_alert_release2, args=(recording_on,))
    p5 = Process(target=pod_alert_performance, args=(recording_on,))
    p1.start() 
    p2.start() 
    p3.start()
    p4.start()
    p5.start()
    app.run(debug=True, use_reloader=False)
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

       
