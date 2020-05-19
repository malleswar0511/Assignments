#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:52:38 2020

@author: mahi
"""
#Write a program to find maximum between two numbers with and  without using conditional operator..py

def largest_Number(a, b): 
    return a * (bool)(a // b) +b * (bool)(b // a) 
a =int(input("enter a value :")) 
b =int(input("enter b value : ")) 
print(largest_Number(a, b))



def largest_number(x,y):
    if (x>y):
        print(x,"is grater than",y)
    else:
        print(y ,"is smaller than",x)
x=int(input("enter x value:"))
y=int(input("enter y value:"))
print(largest_number(x,y))




n=int(input("enter first number :"))
m=int(input("enter second value :"))
largest_number=n if n>m else m
print(largest_number)

