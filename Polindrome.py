# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:16:24 2020

@author: DELL
"""

str=input("enter a string :")
str=str.casefold()
if (str==str[::-1]):
    print("it is a polindrome")
else:
    print("it is not a polindrome")
    
    
    
string=input("Enter a string :")
if (string==string[::-1]):
    print("Polindrome")
else:
    print("not a polindrome")