#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:07:07 2020

@author: mahi
"""
"""
Please write a program to output a random 
even number between 0 and 10 
inclusive using random module and list comprehension.
"""

import random
list1=[random.randrange(1,11) for i in range(1,11) if i%2==0]
print(list1)