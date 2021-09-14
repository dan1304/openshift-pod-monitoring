import sqlite3


#Access database
conn = sqlite3.connect('database.db')

conn.execute('''CREATE TABLE IF NOT EXISTS pod_status
		(ID INTEGER PRIMARY KEY,
		app_name TEXT,
        pod_status TEXT,
        failed_count INTERGER DEFAULT 0
		)''')

conn.execute('''INSERT INTO pod_status
        (app_name, pod_status) 
        VALUES
        (?,?)''', ("mms-api-gateway","OK"))

conn.close()

