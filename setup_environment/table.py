import mysql.connector as sql
import json
import os

curdir = str(os.path.abspath(os.curdir)) + '\\password.json'

with open(curdir, 'r') as openfile:
    credsdic = json.load(openfile)

conn = sql.connect(host='localhost', user='root', passwd=credsdic["databasepsswd"], database='bank')

if conn.is_connected():
     print('connected successfully')
cur = conn.cursor()

cur.execute('create table customer_details(acct_no int primary key,acct_name varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(25),cr_amt float )')

conn.commit()
conn.close()
cur.close()