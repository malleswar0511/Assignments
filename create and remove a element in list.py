#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:58:58 2020

@author: mahi
"""

x=int(input("enter a value :"))
list1=[]
for i in range(0,x):
    list1.append(i)
print(list1)
print("the element removed from the list1 is ",list1.pop())
print(list1)
