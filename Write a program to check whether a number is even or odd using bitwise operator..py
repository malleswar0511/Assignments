#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:54:56 2020

@author: mahi
"""

def odd_even(n):
    if (n&1==1):
        print("odd")
    else:
        print("even")
n=int(input("enter a number :"))
odd_even(n)
