#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:58:24 2020

@author: mahi
"""

num=int(input("enter a number :" ))
if (num&1):
    print("lsb is set")
else:
    print("lsb is not set")
 
""" Most significant bit """

def setbit_number(num):
    num|=num>>1
    num|=num>>2
    num|=num>>4
    num|=num>>8
    num|=num>>16
    num=num+1
    return (num>>1)
num=int(input("enter a number :"))
print(setbit_number(num))
    
    
    












































