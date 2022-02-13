import  mysql.connector as sql
import json
import os

curdir = str(os.path.abspath(os.curdir)) + '\\password.json'

with open(curdir, 'r') as openfile:
    credsdic = json.load(openfile)

conn = sql.connect(host='localhost', user='root', passwd=credsdic["databasepsswd"], database='bank')
cur = conn.cursor()
cur.execute('create table user_table(username varchar(25) PRIMARY KEY, passwrd varchar(25) NOT NULL )')
conn.commit()
conn.close()
cur.cllose()
