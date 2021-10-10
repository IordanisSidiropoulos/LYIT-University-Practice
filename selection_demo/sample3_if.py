"""
#
# File            : sample3_if.py
# Creted          : 09/10/2021 11:20 a.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""


if __name__ == '__main__':

    grade = input("Enter a grade")

    #print("enter a value")
    #grade = input()         #This is the same as above

    grade = int(grade)  # type cast - change the string name to an integer and put it back in
    # the same variable!

    module_1 = "python"

    if grade >= 70 and module_1 == "python":
        print("You rock")
    elif grade >= 60:
        print("You are still good")
    elif grade >= 50:
        print("You are ok")
    elif grade >= 40:
        print("You are at the edge of disaster")
    else:
        print("Change job :|")

