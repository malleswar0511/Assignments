#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:20:15 2020

@author: mahi
"""

def generate_list():
    list1=[]
    for x in range(1,21):
        square=int(x**2)
        list1.append(square)
    print(list1)
generate_list()