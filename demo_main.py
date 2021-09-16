# import time
# from flask import Flask
# from multiprocessing import Process, Value
# import googlechat
# from PodDataCollect import *
# import logging
# import ipdb

# app = Flask(__name__)
# logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# gg_msg = ''

# @app.route('/staging', methods=['GET'])
# def pod_alert_staging(loop_on):
#     app_list = []
#     with open("app_list_env.txt", 'r') as f:
#         for line in f:
#             app = line.split()
#             app_list.append(app)
#     while True:
#         try:
#             for app in app_list:
#                 app_name = app[0]
#                 print(f"App to check: {app_name} ")
#                 pod_info = PodDataCollect(app_name, 0, "equator-default-staging")
#                 shell_cmd = pod_info.shell_cmd()
#                 print(shell_cmd)
#                 pod_status = pod_info.get_pods(shell_cmd)
#                 if 'true' not in str(pod_status):
#                     pod_info.increase_count()
#                     failed_count = pod_info.get_failed_count()
#                     if failed_count[0] >= 3:
#                         googlechat.send_google_chat(pod_status, app_name, "equator-default-staging")
#                 else:
#                     pod_info.reset_count()
#             time.sleep(3)
#         except AttributeError:
#             print("Check param if not passed...")
#         except:
#             print("Something wrong!")

# @app.route('/dev', methods=['GET'])
# def pod_alert_dev(loop_on):
#     app_list = []
#     with open("app_list_env.txt", 'r') as f:
#         for line in f:
#             app = line.split()
#             app_list.append(app)
#     while True:
#         try:
#             for app in app_list:
#                 app_name = app[0]
#                 print(f"App to check: {app_name} ")
#                 pod_info = PodDataCollect(app_name, 0, "equator-default-dev")
#                 shell_cmd = pod_info.shell_cmd()
#                 print(shell_cmd)
#                 pod_status = pod_info.get_pods(shell_cmd)
#                 if 'true' not in str(pod_status):
#                     pod_info.increase_count()
#                     failed_count = pod_info.get_failed_count()
#                     if failed_count[0] >= 3:
#                         googlechat.send_google_chat(pod_status, app_name, "equator-default-dev" )
#                 else:
#                     pod_info.reset_count()
#             print("Idle for next 5 mins....")        
#             time.sleep(300)
#         except AttributeError:
#             print("Check param if not passed...")
#         except:
#             print("Something wrong!")
    
# if __name__ == "__main__":
#     recording_on = Value('b', True)
#     p1 = Process(target=pod_alert_staging, args=(recording_on,))
#     p2 = Process(target=pod_alert_dev, args=(recording_on,))
#     p1.start() 
#     p2.start() 
#     app.run(debug=True, use_reloader=False)
#     p1.join()
#     p2.join()

       
