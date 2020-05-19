#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:07:14 2020

@author: mahi
"""
#write a program to find the GCD or HCF of any number

def hcf(a,b):
    if (a==0):
        return b
    if (b==0):
        return a
    if (a==b):
        return a
    if (a>b):
        return hcf(a-b,b)
    return hcf(a,b-a)
a=int(input("enter a value:"))
b=int(input("enter b value :"))
if (hcf(a,b)):
    print("hcf of a and b is ",hcf(a,b))
else:
    print("not found")
    
    
