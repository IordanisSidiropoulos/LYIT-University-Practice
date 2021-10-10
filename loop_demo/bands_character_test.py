"""
#
# File            : bands_character_test.py
# Created          : 10/10/2021 8:34 p.m.
# Author          : Iordanis Sidiropoulos
# Version         : v1.0.0
# Licencing       : (C) 2021 iordAnis Sidiropoulos, iordanisMusic.com
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':
    bands = input("\nHi\nEnter your favourite band and we will tell you who you are: ")
    bands = str(bands)
    if (bands == "Iron Maiden") or (bands == "iron maiden") or (bands == "ironmaiden") or (bands == "maiden"):# or "iron maiden" or "ironmaiden":
        print("You rock and it is cold on the top!!")
    elif (bands == "Metallica") or (bands == "metallica") or (bands == "metalica"):
        print("Not too bad!!")
    elif (bands == "Scorpions") or (bands == "scorpions"):
        print("You are elegant and some times dirty...!  ;)")
    elif (bands == "Guns n´ Roses") or (bands == "guns n roses") or (bands=="guns n´ roses") or (bands=="Guns n Roses"):
        print("Naughty!! Very naughty!! Bad bad bad YOU!")


    else:
        print("better listen to shakira")