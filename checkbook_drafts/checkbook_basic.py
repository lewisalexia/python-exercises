#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import subprocess
import sys

print(f"Hi, my name is George. How may I help you today?" )
print()
print(f"Please select from the following: ")
print()
print(f"Enter 1 for Deposit\n" "Enter 2 for Withdrawal\n" "Enter 3 for Check Balance\n" "Enter 4 to Exit")
print()

with open('george_write.txt') as f:
    balance = f.read()
    
print(f"Current Balance: ${balance}") 

# main menu below


while True:
    try:
        selection = int(input("Selection: "))
        assert selection <= 4 and selection >0
    except ValueError:
        print("Sorry, I didn't understand that. Please input a selection between 1 and 4.")
        continue
    except AssertionError:
        print("Sorry, I didn't understand that. Please input a selection between 1 and 4.")
        continue
    else:
        break

# deposit function below

if selection == 1:
    deposit_amount = int(input("How much would you like to deposit? We don't care about pennies here. "))
    if deposit_amount >=0:
        balance = int(balance) + deposit_amount
        print()
        print(f"Your balance is: ${balance}")
        with open('george_write.txt', 'w') as f: #overwriting
            f.write(str(balance))    
          
    if deposit_amount == str():
        print(f"Your input is not correct. Please input a number like this, 100: ")
        
# withdrawal function below

if selection == 2:
    withdrawal_amount = int(input("How much would you like to withdraw? We don't care about pennies here. "))
    if withdrawal_amount >=0:
        balance = int(balance) - withdrawal_amount
        print()
        print(f"Your balance is: ${balance}")
        with open('george_write.txt', 'w') as f: #overwriting
            f.write(str(balance))

    if withdrawal_amount == str():
        print(f"Your input is not correct. Please input a number like this, 100: ")

# check balance function below
print()
if selection == 3:
    print(f"Your balance is: ${balance}")
    print()
    print(f'Thank you, goodbye')
# exit function below

if selection == 4:
    with open('george_write.txt', 'w') as f: # appending not overwriting
        f.write(str(balance))
    print('Thank you for the visit, see you later!')

# answer = None 
# while answer not in ("yes", "no"): 
#     answer = str.lower((input(f"Would you like to continue? ")))
#     if answer == "yes":
#         print('Grabbing your request now.')
#     elif answer == "no": 
#         print('Thank you, goodbye')
#     else: 
#         print("Sorry, I didn't understand that. Please input a Yes or a No.")
#         break


# In[ ]:




