"""
#
# File            : while_demo.py
# Created          : 09/10/2021 4:30 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':
    # sample while loop
    max = 5
    counter = 0
    total = 0
    while counter <= max:
        total += 9.99 # book price
        counter += 1 # count of books is incremented
    print("The final amount is: {0:5.2f}".format(total))
