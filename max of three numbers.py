#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:13:36 2020

@author: mahi
"""
#Write a program to find maximum between three numbers using conditional operator.

def maximum_number(x,y,z):
    if x>y and x>z:
        print(x,"is grater than",y,z)
    elif y>z:
        print(y," is grater than",z,x)
    else:
        print(z,"is grater than",y,x )
x= int(input("enter x value: "))
y=int(input("enter y value: "))
z=int(input("enter z value: "))
number=maximum_number(x,y,z)
print(number)
