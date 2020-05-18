#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:51:34 2020

@author: mahi
"""

def character_alphabet(n):
    if((n>='a' and n<='z')or(n>='A' and n<='Z')):
        print(n,"is a alphabet")
    elif n is int:
        print("it is not an alphabet")
    else:
        print("it is not a alphabet")
n=input("enter a character : ")
character_alphabet(n)
