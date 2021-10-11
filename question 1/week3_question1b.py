"""
#
# File            : week3_question1b.py
# Created          : 11/10/2021 2:24 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

print("\n\nWelcome to our new game!\n")

if __name__ == '__main__':

   text: ""
   while 1:
       print("Enter a number from 0 to 11 : ")
       number = input()
       number = int(number)
       if number != 10:
           answer = input("Sorry! Failed! Try again?? 'yes' or 'no' : ")
           answer = str(answer)
           if answer != "yes": print("TRY a Number AGAIN: ")
           break



       if number == 10:
         print("Well Done!!")
         break
