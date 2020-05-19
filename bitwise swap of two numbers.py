#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:53:10 2020

@author: mahi
"""
#Write a program to swap two numbers using bitwise operator

x=int(input("enter first value : "))
y=int(input("enter second value: "))
print("Before swaping two numbers : a={0} and b={1}".format(x,y))
x=x^y
y=x^y
x=x^y
print("After swaping two numbers : a={0} and b={1}".format(x,y))
