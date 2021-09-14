# import time
# from flask import Flask
# from multiprocessing import Process, Value
# import subprocess
# import googlechat
# from podStatus import podStatus
# # import ipdb

# app = Flask(__name__)
# gg_msg = ''
# nested_app_list = {
# 					'mms-api-gateway': {'failed_count': 0},
# 					'mms-centralize-config': {'failed_count': 0}
#                 }
# #ipdb.set_trace()


# for app_name, failed_count in  nested_app_list.items():
#     print(app_name, failed_count)

# shell_cmd = "oc get pod -l appName=mms-spi-engine -o json '--sort-by=.status.containerStatuses[0].state.running.startedAt' | jq -r '.items[0].status.containerStatuses[0].ready' "

# @app.route('/pods', methods=['GET'])
# def get_pods():
#     pod_status = subprocess.check_output(shell_cmd, shell=True, stderr=subprocess.STDOUT)
#     return pod_status

# def pod_alert(gg_msg):
#     while True:
#         gg_msg = get_pods()
#         print(shell_cmd)

#         if 'true' not in str(gg_msg):
#             googlechat.send_google_chat(gg_msg)
#         else:
#             pass
#         time.sleep(160)


# if __name__ == "__main__":
#    recording_on = Value('b', True)
#    p = Process(target=pod_alert, args=(recording_on,))
#    p.start()  
#    app.run(debug=True, use_reloader=False)
#    p.join()

       
