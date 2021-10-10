"""
#
# File            : practice_MYSeLF.py
# Created          : 10/10/2021 5:51 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':
    from string import ascii_lowercase

   # for i in range (20,1,-2):
    #    print(i, end="")

    #sentence = '''Hello World of coding'''

    #for ch in sentence:
     #   if (ch != "o") and (ch != "d"):
      #      print(ch, end="")



    #for i in range(1,10):
    #    if i == 5:
     #    print("HI")
      #  print("N/A")
#print("found in 5")

      #for ch in range(1,20, 2):
       #   if ch == 9:
        #   print("NINEEEEEEE")
         # print("no problem")
#print("\nThat was an example of a basic loop")

    #for ch in range(1, 20):
     #   if ch != 2:
      #      print(ch)

    bands = input("\nHi\nEnter your favourite band and we will tell you who you are: ")
    bands = str(bands)
    if (bands == "Iron Maiden") or (bands == "iron maiden") or (bands == "ironmaiden") or (bands == "maiden"):# or "iron maiden" or "ironmaiden":
        print("You rock and it is cold on the top!!")
    elif (bands == "Metallica") or (bands == "metallica") or (bands == "metalica"):
        print("Not too bad!!")

    else:
        print("better listen to shakira")
