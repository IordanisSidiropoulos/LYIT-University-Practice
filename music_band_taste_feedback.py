"""
#
# File            : music_band_taste_feedback.py
# Created          : 10/10/2021 10:52 p.m.
# Author          : iordAnis Sidiropoulos
# Version         : v1.0.0
# Licencing       : (C) 2021 Iordanis Sidiropoulos, iordanismusic.com
#                   Availaable under GNU Public License (GPL)
# Description     : Have fun by getting a feedback on your music taste!
#
"""
if __name__ == '__main__':
    band = input("Enter your favorite Music Band here!! : ")
    band = str(band)
    band = band.lower()

    if (band == "metallica") or (band == "metalica"):
        print("Not too Bad!")
    elif (band == "guns n roses") or (band == "guns 'n' roses") or (band == "guns n' roses"):
        print("Bad and dirty you are!")
    elif band == "iron maiden":
        print("You are a world class champion!! An exception of humankind!!")
    elif band == "scorpions":
        print("You are elegant...but some times dirty though!! :P ")
    elif band == "nightwish" or band == "night wish":
        print("You were a soprano singer during your previous life! :P ")
    else:
        print("You´d better listen to Shakira!")