"""
#
# File            : music_grade.py
# Created          : 10/10/2021 10:37 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""
if __name__ == '__main__':
    grade = input("Enter your music Grade")
    grade = int(grade)

    if grade < 40:
        print("Change job")
    elif 40 <= grade < 50:
        print("Biological sound tissue destruction you are !%3%·%!!")
    elif 50 <= grade < 60:
        print("You hurt my ears")
    elif 60 <= grade < 70:
        print("Pass")
    elif 70 <= grade < 80:
        print("Good Pass")
    elif 80 <= grade < 90:
        print("Professional")
    elif 90 <= grade <= 100:
        print("World Class Musician")