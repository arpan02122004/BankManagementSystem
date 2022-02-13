import  mysql.connector as sql
import json
import os

curdir = str(os.path.abspath(os.curdir)) + '\\password.json'

with open(curdir, 'r') as openfile:
    credsdic = json.load(openfile)
    
conn=sql.connect(host='localhost', user='root', passwd=credsdic["databasepsswd"], database='bank')
cur = conn.cursor()
cur.execute('create table transactions(acct_no int(11),date date ,withdrawal_amt bigint(20),amount_added bigint(20) )')

conn.commit()
conn.close()
cur.cllose()
