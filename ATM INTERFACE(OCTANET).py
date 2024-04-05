#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import getpass
import string
import os
from datetime import datetime

# creating lists of users, their PINs, bank statements, and transaction history
users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
transaction_history = [[] for _ in range(len(users))]  # List to store transaction history for each user
count = 0

# while loop checks existence of the entered username
print("****************************************************************************")
print("*                                                                          *")
print("*                         Welcome to ATM MACHINE                           *")
print("*                                                                          *")
print("****************************************************************************")
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        n = users.index(user)  # Getting the index of the user
        break
    else:
        print('----------------')
        print('****************')
        print('INVALID USERNAME')
        print('****************')
        print('----------------')

# comparing pin
while count < 3:
    print('------------------')
    print('******************')
    pin = input('PLEASE ENTER PIN: ')
    print('******************')
    print('------------------')
    if pin.isdigit():
        if pin == pins[n]:
            break
        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()
    else:
        print('------------------------')
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        print('------------------------')
        count += 1

# in case of a valid pin - continuing, or exiting
if count == 3:
    print('-----------------------------------')
    print('***********************************')
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')
    print('-----------------------------------')
    exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESSFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
    # os.system('clear')
    print('-------------------------------')
    print('*******************************')
    response = input(
        'SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nDeposit__(D)  \nChange PIN_(P)  \nTransaction History(T)\nQuit_______(Q) \nType The Letter Of Your Choices: ').lower()
    print('*******************************')
    print('-------------------------------')
    valid_responses = ['s', 'w', 'd', 'p', 't', 'q']
    response = response.lower()
    if response == 's':
        print('---------------------------------------------')
        print('*********************************************')
        print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n], 'RUPEES ON YOUR ACCOUNT.')
        print('*********************************************')
        print('---------------------------------------------')

    elif response == 'w':
        print('---------------------------------------------')
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('*********************************************')
        print('---------------------------------------------')
        if cash_out % 10 != 0:
            print('------------------------------------------------------')
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 RUPEES NOTES')
            print('******************************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
            print('-----------------------------')
        else:
            amounts[n] -= cash_out
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_history[n].append(('Withdrawal', cash_out, timestamp))  # Adding withdrawal transaction to history
            print('-----------------------------------')
            print('***********************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('***********************************')
            print('-----------------------------------')

    elif response == 'd':
        print()
        print('---------------------------------------------')
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
        print('*********************************************')
        print('---------------------------------------------')
        print()
        if cash_in % 10 != 0:
            print('----------------------------------------------------')
            print('****************************************************')
            print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 RUPEES NOTES')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amounts[n] += cash_in
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_history[n].append(('Deposit', cash_in, timestamp))  # Adding deposit transaction to history
            print('----------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
            print('****************************************')
            print('----------------------------------------')
    elif response == 'p':
        print('-----------------------------')
        print('*****************************')
        new_pin = int(input('ENTER A NEW PIN: '))
        print('*****************************')
        print('-----------------------------')
        print('------------------')
        print('******************')
        new_ppin = int(input('CONFIRM NEW PIN: '))
        print('*******************')
        print('-------------------')
        if new_ppin != new_pin:
            print('------------')
            print('************')
            print('PIN MISMATCH')
            print('************')
            print('------------')
        else:
            pins[n] = new_pin
            print('************')
            print('------------')
            print('NEW PIN SAVED')
            print('************')
            print('------------')
    elif response == 't':  # Option to view transaction history
        print('----------------------------------------')
        print('********* TRANSACTION HISTORY *********')
        print('----------------------------------------')
        for idx, transaction in enumerate(transaction_history[n], start=1):
            trans_type, amount, timestamp = transaction
            print(f'{idx}. {trans_type}: {amount} RUPEES at {timestamp}')
        print('----------------------------------------')
    elif response == 'q':
        exit()
    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')



# In[ ]:




