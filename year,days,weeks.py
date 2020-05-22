#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 06:21:44 2020

@author: mahi
"""

n=int(input("enter number of days :"))
year=int(n/365)
week=int((n%365)/7)
days=int(n%365)%7
print("year :",year,"\nweek :",week,"\ndays :",days)