"""
#
# File            : sample2_if.py
# Creted          : 09/10/2021 11:20 a.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':
    grade = 30
    module_1 = "python"

    if grade >= 70 and module_1 == "python":
        print("You have earned a Distinction") #comments can be placed enywhere!
        #Comments should be included to explain
        # all interesting sctions of code!
    elif grade >= 60:
        print("You are still good")
    elif grade >= 50:
        print("You are ok")
    elif grade >= 40:
        print("Come on! You could be better man!")
    else:
        print("Change job :|")
