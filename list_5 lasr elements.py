#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 21:41:32 2020

@author: mahi
"""
            
def generate_list():
    list1=[]
    for i in range(1,21):
        list1.append(i*i)
    print(list1)
    print(list1[-6:-1])
generate_list()