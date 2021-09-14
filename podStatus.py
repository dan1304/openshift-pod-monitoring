import subprocess



class podStatus:
    global shell_cmd
    global app_name

    def __init__(self, app_name, failed_count):
        self.app_name = app_name
        self.failed_count = failed_count

    shell_cmd = f"oc get pod -l appName=mms-api-gateway -o json '--sort-by=.status.containerStatuses[0].state.running.startedAt' \
                  | jq -r '.items[0].status.containerStatuses[0].ready' "

    def get_pods(self):
        self.pod_status = subprocess.check_output(shell_cmd, shell=True, stderr=subprocess.STDOUT)
        print(self.app_name, self.failed_count, self.pod_status)
        print(f"TuyenTD: {shell_cmd}")
        return self.pod_status

