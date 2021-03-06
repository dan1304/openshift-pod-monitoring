import sqlite3

app_list = []
with open("app_list_to_check.txt", 'r') as f:
    for line in f:
        app = line.split()
        app_list.append(app)

env_list = ("equator-default-staging",
            "equator-default-release1",
            "equator-default-release2",
            "equator-default-performance",
            "equator-sandbox-dev"
            )

#Access database
conn = sqlite3.connect('database.db')
conn.execute('''CREATE TABLE IF NOT EXISTS pod_status
		(ID INTEGER PRIMARY KEY,
		app_name TEXT,
        environment TEXT,
        failed_count INTERGER DEFAULT 0
		)''')
conn.close()

for app in app_list:
    print(app)
    app_name = app[0]
    for env in env_list:
        print(env)
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute('''INSERT INTO pod_status 
                            (app_name, environment) 
                            VALUES (?,?)''', (app_name, env))
        conn.close()
