#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:04:23 2020

@author: mahi
"""
def Numgenerator(n):
    for i in range(n+1):
        if(i%5==0 and i%7==0):
            yield i
n=int(input("enter a number :"))
list1=[] 
for i in Numgenerator(n):
    list1.append(str(i))
print(",".join(list1))