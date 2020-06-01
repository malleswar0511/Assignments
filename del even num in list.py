#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:11:16 2020

@author: mahi
"""

list1=[5,6,77,45,22,12,24]
list2=[]
for i in list1:
    if i%2==1:
        list2.append(i)
        list2.sort()
print(list2)
    