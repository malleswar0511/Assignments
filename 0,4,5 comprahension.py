#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 19:56:47 2020

@author: mahi
"""
list1=[12,24,35,70,88,120,155]
print([i for (n,i) in enumerate(list1) if n not in (0,4,5)])
