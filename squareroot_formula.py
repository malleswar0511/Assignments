#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 05:12:15 2020

@author: mahi
"""

import math
c=50
h=30
list1=[]
ele=[i for i in input().split(',')]
for d in ele:
    list1.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(list1))
