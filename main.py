from flask import Flask
from multiprocessing import Process, Value
from PodDataCollect import *
from PodStatusCheck import *
import logging, os
from dotenv import load_dotenv
import subprocess, sys
import database

load_dotenv(".env")
OCP_URL = os.getenv('OCP_URL')
OC_USER = os.getenv('OC_USER')
OC_PASSWORD = os.getenv('OC_PASSWORD')

app = Flask(__name__)
# logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
root = logging.getLogger()
root.setLevel(logging.DEBUG)

# logging to stdout
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

# login OCP3 Non prod (no need if we export KUBE_CONFIG in dockerfile)
ocp_login = f"oc login --config /tmp/config {OCP_URL} -u={OC_USER}  -p={OC_PASSWORD} --insecure-skip-tls-verify=true"
logging.info(f"OCP login: {ocp_login}")
subprocess.check_output(ocp_login, shell=True, stderr=subprocess.STDOUT)

# read app list to check
app_list_file = "app_list_to_check.txt"

@app.route('/staging', methods=['GET'])
def pod_alert_staging():
    staging_pods = PodStatusCheck(app_list_file, "equator-default-staging")
    staging_pods.check_app_status()

@app.route('/sandbox', methods=['GET'])
def pod_alert_dev():
    dev_pods = PodStatusCheck(app_list_file, "equator-sandbox-dev")
    dev_pods.check_app_status()    

@app.route('/release1', methods=['GET'])
def pod_alert_release1():
    release1_pods = PodStatusCheck(app_list_file, "equator-default-release1")
    release1_pods.check_app_status() 

@app.route('/release2', methods=['GET'])
def pod_alert_release2():
    release2_pods = PodStatusCheck(app_list_file, "equator-default-release2")
    release2_pods.check_app_status()    

@app.route('/performance', methods=['GET'])
def pod_alert_performance():
    performance_pods = PodStatusCheck(app_list_file, "equator-default-performance")
    performance_pods.check_app_status()    

if __name__ == "__main__":
    recording_on = Value('b', True)
    # for p_name in ("pod_alert_staging", "pod_alert_release1", "pod_alert_release2", "pod_alert_sandbox", "pod_alert_performance" ):
    #     p = Process(target=p_name)
    #     p.start()
    #     p.join()
    # app.run(debug=True, use_reloader=False)
    p1 = Process(target=pod_alert_staging)
    p2 = Process(target=pod_alert_dev)
    p3 = Process(target=pod_alert_release1)
    p4 = Process(target=pod_alert_release2)
    p5 = Process(target=pod_alert_performance)
    p1.start(); 
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

       
