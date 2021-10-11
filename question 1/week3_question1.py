"""
#
# File            : week3_question1.py
# Created          : 10/10/2021 10:09 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""



if __name__ == '__main__':
   # for i in range(1, 10):
    #    if i == 6:
     #      print("CIAOOOOO!! :D :D")
      #     break
       # print("hi")
    #print("Found at {}".format(i))

#   text = ""
#   while 1:
#    print("Enter name")
#    uname = input()
#    if (uname == "joe"):
#      break
#   print("Finished")
   print("\n\nWelcome to our new game!\n")
   text: ""
   while 1:
       print("Enter a number from 0 to 10 : ")
       number = input()
       number = int(number)
       if number != 10:
             answer = input("Sorry! Failed! Try again?? 'yes' or 'no' : ")
             #answer = str(answer)
             if answer == "no": print("Thank you for trying! Goodbye!")
             break
             if answer == "yes": print("AGAIN now....")



       if number == 10:
        print("Well Done!!")
        break

