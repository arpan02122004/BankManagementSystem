import mysql.connector as sql
import datetime as dt

conn = sql.connect(host='localhost', user='root', passwd='manager', database='bank')
cur = conn.cursor()

print('=========================WELCOME TO STARK BANK============================================================')

print(dt.datetime.now())
print('1.REGISTER')
print()
print('2.LOGIN')
print()

n = int(input('enter your choice='))
print()

if n == 1:
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
