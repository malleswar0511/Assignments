#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 07:30:20 2020

@author: mahi
"""
class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self)
        self.length=length
    def area(self):
        return self.length*self.length
n=int(input("enter a number : "))
square=Square(n)
print(square.area())
            
        
        