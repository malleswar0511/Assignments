#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:47:57 2020

@author: mahi
"""

def gcd(a,b):
    if a ==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return (a*b)/gcd(a,b)
a=15
b=15
print("lcm of",a,"and",b,"is",lcm(a,b))
