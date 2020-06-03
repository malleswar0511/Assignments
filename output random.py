#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:47:16 2020

@author: mahi
"""
import random
print(random.choice([x for x in range(11) if x%5==0 and  x%7==0]))