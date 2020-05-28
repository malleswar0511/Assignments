#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:54:43 2020

@author: mahi
"""
angle1=int(input("enter angle1: "))
angle2=int(input("enter angle2 :"))
angle3=180-(angle1+angle2)
if angle1>=180:
    print("its is not a triangle")
elif  angle2>=180:
    print("its not a triangle")
else:
    print("angle3 :",angle3)