#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 07:00:56 2020

@author: mahi
"""
items = []
num = [x for x in input("enter a binary number").split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print("the divisible binary number is ",','.join(items))
