#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:38:02 2020

@author: mahi
"""

list1= []
for i in range(1000, 3001):
    string= str(i)
    if (int(string[0])%2==0) and (int(string[1])%2==0) and (int(string[2])%2==0) and (int(string[3])%2==0):
        list1.append(string)
print (",".join(list1))