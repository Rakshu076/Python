
"""
1. Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
a=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        a.append(i)
print(a)

"""
2. Write a Python program to accept the user's first and last name
 and then getting them printed in the the reverse order
 with a space between first name and last name.
"""

First= input('enter the first name')
Last= input('enter the last name')
print(First[::-1] + ' '+ Last[::-1])

'''
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3
'''
import math
diameter=12
r=diameter/2
volume=4/3*math.pi*r**3
print(volume)

'''
Task 2
1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list.
'''
integer=input('enter the numbers with csv')
print(integer.split(','))

'''
2. Create the below pattern using nested for loop in Python.
'''
for i in range(5):
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(5,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()

'''
3. Write a Python program to reverse a word after accepting the input from the user.
'''
user_input= input('Enter the word ')
print(user_input[::-1])

'''
4. Write a Python Program to print the given string in the format specified in the ​sample output.
 WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST,
 SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens
'''
print('WE,THE PEOPLE OF INDIA,\n \thaving solemnly resolved to constitute India into a SOVEREIGN,!\n \t \tSOCIALIST, '
      'SECULAR,DEMOCRATIC REPUBLIC \n \t\t\tand to secure to all its citizens')

