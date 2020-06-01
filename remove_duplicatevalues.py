#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 06:52:31 2020

@author: mahi
"""
list1=[12,24,35,24,88,120,155,88,120,155]
my_list=list(dict.fromkeys(list1))
my_list.sort()
print(my_list)

