#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 07:12:01 2020

@author: mahi
"""

frequent = {}   
line = input("enter a string :")
for word in line.split():
    frequent[word] = frequent.get(word,0)+1
words = frequent.keys()
for w in words:
    print ("%s:%d" % (w,frequent[w]))