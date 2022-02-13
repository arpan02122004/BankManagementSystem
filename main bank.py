import mysql.connector as sql
import datetime as dt
import json
import base64

with open('password.json', 'r') as openfile:
    credsdic = json.load(openfile)

conn = sql.connect(host='localhost', user='root', passwd=credsdic["databasepsswd"], database='bank')
cur = conn.cursor()

print('=========================WELCOME TO ARPAN BANK============================================================')

print(dt.datetime.now())
print('1.REGISTER\n')
print('2.LOGIN\n')

n = int(input('enter your choice='))
print()

if n == 1:
    print("Authentication.....")
    password_admin = input("Enter admin password : ")
    if str(base64.b64encode(password_admin.encode('utf-8'))) == str(credsdic['adminaccess']):
        name = input('Enter a Username=')
        print()
        passwd = int(input('Enter a 4 DIGIT Password='))
        print()
        V_SQLInsert = "INSERT  INTO user_table (passwrd,username) values (" + str(passwd) + ",' " + name + " ') "
        cur.execute(V_SQLInsert)
        conn.commit()
        print()
        print('USER created successfully')
        import menu
    else:
        print("\n INCORRECT PASSWORD \n ")

if n == 2:
    name = input('Enter your Username=')
    print()
    passwd = int(input('Enter your 4 DIGIT Password='))
    V_Sql_Sel = "select * from user_table where passwrd='" + str(passwd) + "' and username=  ' " + name + " ' "
    cur.execute(V_Sql_Sel)
    if cur.fetchone() is None:
        print()
        print('Invalid username or password')
    else:
        print()
        import menu
