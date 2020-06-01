#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 07:10:52 2020

@author: mahi
"""

list1=[1,2,3,4,5,6,7,8,9,10]
even_number=lambda x :x%2==0
list2=list(filter(even_number,list1))
print(list2)