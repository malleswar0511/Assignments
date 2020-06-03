#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:59:47 2020

@author: mahi
"""
import random
print(random.sample([i for i in range(100,201) if i%2==0],5))