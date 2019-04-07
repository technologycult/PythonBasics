'''
Python Basics - Session # 9

Topic to be covered - 
1. Receiving inputs in Python
2. Type conversion
'''

name = input('enter your name : ')
print(name)
favourite_food = input('enter your favourite food : ')
print(name + ' loves ' + favourite_food)

################################################

account_balance = 50000

salary = input('enter the salary credited : ')
final_balace = account_balance + int(salary)
print('Final amount in the account :',final_balace)

################################################
''' celcius to farenheit conversion '''

temp_in_celcius = int(input('enter the temp in celcius : '))
print('Temperature entered in celcius is :', temp_in_celcius)

#C/5 = (F-32)/9

#F = 9 * C/5 + 32

temp_in_farenhiet = 9 * temp_in_celcius/5 + 32

print('temp in harenheit is :', temp_in_farenhiet)























