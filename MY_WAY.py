"""
#
# File            : MY_WAY.py
# Created          : 11/10/2021 6:48 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

print("\nWelcome to our Game!\n")


# number = input("Please, enter a number from 0 to 10 here: ")
# number = int(number)

if __name__ == '__main__':
    text = ""
    while 1:
        number = input("Please, enter a number from 0 to 10 here: ")
        number = int(number)
        if number != 10:
            answer = input("Sorry - Mistake!! Try again??   :  ")
            answer = str(answer.lower())
            if (answer == "no") or (answer == "n"):
                print("Thank You! Goodbye!")
                break
            if answer == "yes" or "y":
                print("SO, AGAIN....")
            elif answer != "yes" or answer != "y" or answer != "no" or "n":
                print("WE MEANT....") and input
        elif number == 10:
            print("WELL DONE!!")
            break

