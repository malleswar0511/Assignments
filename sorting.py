#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 06:42:01 2020

@author: mahi
"""


from operator import itemgetter
information = []
while True:
    single_info = input()
    if single_info == "":
        break
    else:
        information.append(tuple((single_info.split(","))))
information.sort(key =  itemgetter(0, 1, 2))       
print(information)