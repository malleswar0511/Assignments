# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:57:27 2020

@author: DELL
"""

def cost(meal_cost,tip_percent,tax_percent):
    
    tip=meal_cost*tip_percent/100
    tax=meal_cost*tax_percent/100
    print(round(meal_cost+tip+tax))
if __name__=='__main__':
    meal_cost=float(input("enter meal_cost :"))
    tip_percent=int(input("enter tip : "))
    tax_percent=int(input("enter tax :"))
    cost(meal_cost,tip_percent,tax_percent)