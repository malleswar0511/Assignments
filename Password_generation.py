# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:58:10 2020

@author: DELL
"""

import random
passlen=int(input("enter the length of password : "))

s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p=" ".join(random.sample(s,passlen))
print(p)
