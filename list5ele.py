#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:06:46 2020

@author: mahi
"""

def list_5ele():
    list1=[]
    for i in range(1,21):
        list1.append(i*i)
    print(list1)
    print("removing the first 5 elements :")
    print(list1[5:])
list_5ele()