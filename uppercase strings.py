#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 07:16:18 2020

@author: mahi
"""
class Inoutstring(object):
    def __init__(self):
        self.s= " "
        
    def getstring(self):
        self.s=input("enter some string :")
    def printstring(self):
        print(self.s.upper())
obj=Inoutstring()
obj.getstring()
obj.printstring()