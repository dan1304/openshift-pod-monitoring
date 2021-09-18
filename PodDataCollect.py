import subprocess
import sqlite3

class PodDataCollect:
    def __init__(self, app_name, failed_count, environment):
        self.app_name = app_name
        self.failed_count = failed_count
        self.environment = environment

    def shell_cmd(self):
        self.oc_command = f"oc get pod -n {self.environment} --config /tmp/config -l appName={self.app_name} -o json '--sort-by=.status.containerStatuses[0].state.running.startedAt' \
                  | jq -r '.items[0].status.containerStatuses[0].ready' "        
        return self.oc_command

    def get_pods(self, shell_cmd):
        self.pod_status = subprocess.check_output(shell_cmd, shell=True, stderr=subprocess.STDOUT)
        return self.pod_status

    def get_failed_count(self):
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT failed_count FROM pod_status WHERE app_name=? and environment=?", (self.app_name, self.environment ))
            self.failed_count = cur.fetchone()
        conn.close()
        return self.failed_count

    def increase_count(self):
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("UPDATE pod_status SET failed_count = failed_count+1 WHERE app_name = ? and environment=?", (self.app_name, self.environment ))
        conn.close()

    def reset_count(self):
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("UPDATE pod_status SET failed_count = 0 WHERE app_name = ? and environment=?", (self.app_name, self.environment ))
        conn.close()
