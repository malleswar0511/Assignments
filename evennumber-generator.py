#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:35:28 2020

@author: mahi
"""
def generator(X):
    i=0
    while (i<=n):
        if i%2==0:
            yield i
        i=i+1
n=int(input("enter a number : "))
list1=[]
for i in generator(n):
    list1.append(str(i))
print(",".join(list1))
    
    