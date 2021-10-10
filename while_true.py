"""
#
# File            : while_true.py
# Created          : 10/10/2021 9:06 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':
    #While true sample
    text=""
    while 1:
       print("Enter name")
       uname = input()
       uname = uname.lower()
       if (uname == "iordanis") or (uname == "iordanis sidiropoulos") or (uname == "eleni bakali") or (uname == "eleni"):
           break
       print("\nSorry, bad name! TRY AGAIN! \n")
    print("This is a good name")