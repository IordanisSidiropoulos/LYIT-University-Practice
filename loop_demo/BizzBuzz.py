"""
#
# File            : BizzBuzz.py
# Creted          : 09/10/2021 3:29 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

#if __name__ == '__main__':
    # COMMENT: siplified Bizz Buzz game
 #   for i in range(1,20):
  #      if i == 5:
   #         print("BUZZ")
    #    print("bizz")

#if __name__ == '__main__':
 #   for i in range(1,20):
  #      if (i % 5) == 0:
   #         print("BUZZ")
    #    print("bizz")

#if __name__ == '__main__':
 #   for i in range(1, 22):
  #      if (i % 6) == 1:
   #         print("OUTCH")
    #    print("bizz")

if __name__ == '__main__':
    for i in range (1,20):
        if (i == 6) or (i == 10) or (i==15) and (i == 19):
            print("BUZZZZZ")
            break
        print("bizz")
    print("found at {}".format(i))