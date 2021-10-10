"""
#
# File            : Find_me_example.py
# Creted          : 09/10/2021 4:12 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""


if __name__ == '__main__':
    # Stop when you find a 6
    # Break statement stops the loop
    for i in range(1,10):
        if i == 6:
            print("Found")
            break
        print("Not Yet")
    print("It was found at {}".format(i))

if __name__ == '__main__':
    for i in range(1,7):
        if i == 2:
            print("STOP")
            break
        print("roll")
    print("from 1 to 7")
