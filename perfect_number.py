# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:02:35 2020

@author: DELL
"""
i=1
sum=0
n=int(input("enter a number :"))
while (i<n):
    if (n%i==0):
        sum=sum+1
    i+=1
if (sum==n):
    print(i,"is a perfect number")
else:
    print(i,"is not a perfect number")