#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 06:41:02 2020

@author: mahi
"""

def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print("division by zero")
except Exception:
    print("caught an exception")
finally:
    print("NO EXCEPTIONS")