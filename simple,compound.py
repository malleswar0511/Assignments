#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:43:48 2020

@author: mahi
"""
P = float(input("Enter the principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
Simple_Interest = (P * N * R)/100.
print("Simple interest : {}". format(Simple_Interest))  



def compound_intrest(principal,rate,time):
	com_int=principal*(pow((1+rate/100),time))
	print("compound_intrest is",com_int)
principle=float(input("enter principle : "))
rate=float(input("enter rate of interest :"))
time=float(input("enter number of years :"))

compound_intrest(principle,rate,time)