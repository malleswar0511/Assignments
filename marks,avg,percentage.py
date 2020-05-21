#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 06:31:36 2020

@author: mahi
"""
subject1=int(input("enter subject1 marks : "))
subject2=int(input("enter subject2 marks : "))
subject3=int(input("enter subject3 marks : "))
subject4=int(input("enter subject4 marks : "))
subject5=int(input("enter subject5 marks : "))
total = subject1+subject2+subject3+subject4+subject5
average=total/5
percentage=(total/500)*100
print("total subject marks :",total)
print("average marks :",average)
print("percentage",percentage)