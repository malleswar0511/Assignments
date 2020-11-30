# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:34:55 2020

@author: DELL
"""

def printmenu():
    print("=== Main Menu ===")
    print("1.Display Team players")
    print("2.Add new player")
    print("3.Delete a player")
    print("4.Edit a player")
    print("5.exit program")
players=["Dhana","Prasanth","Rupesh","Sathi"]
while True:
    printmenu()
    choice=int(input("choose a menu option from 1 to 4 or 5 to exit : "))
    if choice==1:
        for i in players:
            print(i)
    if choice==2:
        add=input(r"enter a name to add : ")
        players.append(add)
    if choice==3:
        delete=input(r"enter a name to remove : ")
        players.pop(int(i))
    if choice==4:
        edit=input(r"enter a name to edit : ")
        players[edit]=new_player
        new_player=[i]
    if choice==5:
        break
            