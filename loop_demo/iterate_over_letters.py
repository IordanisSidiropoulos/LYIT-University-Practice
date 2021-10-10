"""
#
# File            : iterate_over_letters.py
# Creted          : 09/10/2021 12:50 p.m.
# Author          : R.G. Lennon
# Version         : v1.0.0
# Licencing       : (C) 2021 Ruth G. Lennon, LYIT
#                   Availaable under GNU Public License (GPL)
# Description     :
#
"""


if __name__ == '__main__':
    from string import ascii_lowercase

    lyrics = """How do you read a madman's mind? Teach me the art of war. For I shall bring more than you 
    bargained for.      Give me an ultimatum that I could not dream of. Spills of a crying nation upon my soul.   
    For I have not a mortal soul, that you already know. Look at my eyes, there's no surprise. 
    Ocean is black, the devil's track, looking beyond, beneath the sea.
    Eye of the storm is here again, been there before you were ever born. Beyond the dark, I feel the pain
    It's hidden but I can't explain. A cross to bear, a heavy faith. My sorrow whispers time again
    
    Lyrics part from: "Stratego"
    by: Iron Maiden"""

    #for ch in ascii_lowercase:
     #   print(ch)

    #for i in ascii_lowercase:print(i, end="")
    #for ch in ascii_lowercase:print(ch, end="|")
    # comment: it does not matter whether it is "i" or "ch" or any letter attributed to it

    # for i in lyrics:
      #  if i != "o":
       #   print(i, end="")

   # for ch in lyrics:
        #print(ch, end="")


    for ch in lyrics:
        if ch != "o":
            print(ch, end="")