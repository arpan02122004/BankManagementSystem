# Importing required lib.
import datetime as dt
import mysql.connector as sql
import json

#loading creadintials
with open('password.json', 'r') as openfile:
    credsdic = json.load(openfile)

# connecting to the sql server
conn = sql.connect(host='localhost', user='root', passwd=credsdic["databasepsswd"], database='bank')
cur = conn.cursor()

conn.autocommit = True
while True:
    # MEnu for user 
    print('\n1.CREATE BANK ACCOUNT\n')
    print('2.TRANSACTION\n')
    print('3.CUSTOMER DETAILS\n')
    print('4.TRANSACTION DETAILS\n')
    print('5.DELETE ACCOUNT\n')
    print('6.QUIT\n')
    n = int(input('Enter your CHOICE : '))
    
    """
    chose the the number of option you want to execute and each if does what is said in front
    of the number
    """
    
    if n == 1:
        cur.execute("Select * from customer_details")
        cur.fetchall()
        acc_no = cur.rowcount + 1
        acc_name = input('\nEnter your ACCOUNT NAME=')
        ph_no = int(input('\nEnter your PHONE NUMBER='))
        add = (input('\nEnter your place='))
        cr_amt = int(input('Enter your credit amount='))
        V_SQLInsert = "INSERT  INTO customer_details values (" + str(acc_no) + ",' " + acc_name + " '," + str(
            ph_no) + ",' " + add + " '," + str(cr_amt) + " ) "
        cur.execute(V_SQLInsert)
        print('\nAccount Created Successfully!!!!!')
        conn.commit()

    elif n == 2:
        acct_no = int(input('Enter Your Account Number='))
        cur.execute('select * from customer_details where acct_no=' + str(acct_no))
        data = cur.fetchall()
        count = cur.rowcount
        conn.commit()
        if count == 0:
            print('\nAccount Number Invalid Sorry Try Again Later\n')
        else:
            print('\n1.WITHDRAW AMOUNT')
            print('\n2.ADD AMOUNT\n')

            x = int(input('Enter your CHOICE='))

            if x == 1:
                amt = int(input('\nEnter withdrawal amount='))
                cr_amt = 0
                cur.execute(
                    'update customer_details set   cr_amt=cr_amt-' + str(amt) + ' where acct_no=' + str(acct_no))
                V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,
                                                                                               dt.datetime.today(), amt,
                                                                                               cr_amt)
                cur.execute(V_SQLInsert)
                conn.commit()
                print('\n Account Updated Successfully!!!!!')

            elif n == 2:
                amt = int(input('Enter amount to be added='))
                cr_amt = 0
                cur.execute('update customer_details set  cr_amt=cr_amt+' + str(amt) + ' where acct_no=' + str(acct_no))
                V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,
                                                                                                dt.datetime.today(),
                                                                                                cr_amt, amt)
                cur.execute(V_SQLInsert)
                conn.commit()
                print('\nAccount Updated Successfully!!!!!')

    elif n == 3:
        acct_no = int(input('Enter your account number='))
        cur.execute('select * from customer_details where acct_no=' + str(acct_no))
        if cur.fetchone() is None:
            print('\n\nInvalid Account number')
        else:
            cur.execute('select * from customer_details where acct_no=' + str(acct_no))
            data = cur.fetchall()
            for row in data:
                print('ACCOUNT NO : ', acct_no, '\n')
                print('ACCOUNT NAME : ', row[1], '\n')
                print(' PHONE NUMBER : ', row[2])
                print('ADDRESS : ', row[3], '\n')
                print('cr_amt : ', row[4], '\n')
    elif n == 4:
        acct_no = int(input('Enter your account number='))
        cur.execute('select * from customer_details where acct_no=' + str(acct_no))
        if cur.fetchone() is None:
            print('\n\nInvalid Account number')
        else:
            cur.execute('select * from transactions where acct_no=' + str(acct_no))
            data = cur.fetchall()
            for row in data:
                print('ACCOUNT NO : ', acct_no, '\n')
                print('DATE : ', row[1], '\n')
                print(' WITHDRAWAL AMOUNT : ', row[2]), '\n'
                print('AMOUNT ADDED : ', row[3], '\n')
    elif n == 5:
        print('DELETE YOUR ACCOUNT')
        acct_no = int(input('Enter your account number : '))

        cur.execute('delete from customer_details where acct_no=' + str(acct_no))
        print('ACCOUNT DELETED SUCCESSFULLY')

    elif n == 6:
        print('DO YO WANT TO EXIT(y/n) : ')
        c = input('enter your choice : ')
        if c.islower() == 'n':
            pass
        else:
            print('THANK YOU PLEASE VISIT AGAIN : ')
            exit()
