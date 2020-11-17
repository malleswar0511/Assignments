# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:20:02 2020

@author: DELL
"""

n=int(input("enter a number : "))
if (n==1):
    print("Weird")
elif n in range(2,6):
    if (n%2==0):
        print("Not Weird")
    else:
        print("Weird")
elif n in range(6,21):
    if (n%2==0):
        print("Weird")
    else:
        print("Not Weird")
else:
    if (n%2==0):
        print("Not Weird")
    else:
        print("Weird")
