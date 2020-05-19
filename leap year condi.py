#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:50:33 2020

@author: mahi
"""
#Write a program to check whether character is an alphabet or not using conditional operator.

def leap_year(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year ".format(year))
    else:
        print("{0} is not a leap year".format(year))
year=int(input("enter a year:"))
leap_year(year)
