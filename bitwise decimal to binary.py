#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:55:51 2020

@author: mahi
"""
#Write a program to convert decimal to binary number system using bitwise operator

def dec_bin(n):
    binary=[0]*n
    i=0
    while(n>0):
        binary[i]=n%2
        n=int(n/2)
        i=i+1
    for j in range(i-1,-1,-1):
        print(binary[j],end= " ")
n=int(input("enter a number : "))
dec_bin(n)

#########


def decimaltobinary(num):
    if num >1:
        decimaltobinary(num//2)
    print(num%2 , end = " ")
number=int(input("enter a number :"))
decimaltobinary(number)


#########

x=int(input("enter a number :"))
bs = " "
while x!=0:
    bs=bs+str(x%2)
    x=x//2
print("decimal - binary") 
for i in range(len(bs)-1,-1,-1):
    print(bs[i],end= " ")
