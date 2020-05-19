#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:39:54 2020

@author: mahi
"""
#program to set nth bit of a number.py

def nth_bit(m,n):
        return ((1<<n|m))
m=int(input("enter a number :"))
n=int(input("enter a value toset nth bit :"))
nth_bit(m,n)
print("nth bit set number is :",nth_bit(m,n))   
