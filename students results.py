#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:48:13 2020

@author: mahi
"""

marks=int(input("enter your marks : "))
if(marks>=70):
    print("distinction")
elif(marks>=60 and marks<70):
    print("First class")
elif(marks>=50 and marks<60):
    print("Second class")
elif(marks>=40 and marks<50):
    print("Third class")
else:
    print("Fail")    
    
   