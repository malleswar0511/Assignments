#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:56:25 2020

@author: mahi
"""

#####   set

myset={"apple","carrot","cherry"}
for item in myset:
    print(item)



set1={1,2,3,4,5,6,7,8,9}
for item in set1:
    print(item)
    
    
    
print("banana" in myset)
print("carrot" in myset)


n = int(input("enter a value : "))
if n&1:
    print("it is an odd number")
else:
    print("it ia an even number")