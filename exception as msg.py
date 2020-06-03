#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 09:38:50 2020

@author: mahi
"""

class exception(Exception):
    def __init__(self,msg):
        self.msg=msg
error=exception("something wrong")
print(error)
        

        
    