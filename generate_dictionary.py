#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 07:20:43 2020

@author: mahi
"""

def generate_dictionary(n):
    dict1={}
    for x in range(1,n):
        dict1[x]=x**2
    print(dict1)
generate_dictionary(n=21)