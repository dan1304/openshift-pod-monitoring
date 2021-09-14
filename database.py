import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table


conn.execute('''CREATE TABLE pod_status
		(ID INTEGER,
		app_name TEXT,
        pod_status TEXT,
        failed_count INTERGER DEFAULT 0
		)''')

conn.close()

