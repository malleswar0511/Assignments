#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:27:28 2020

@author: mahi
"""
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))