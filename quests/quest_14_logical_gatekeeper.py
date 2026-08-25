#!/usr/bin/env python3
GUEST_AGE=int(input("How old are you? "))
NUMBER_OF_COINS=int(input("How many gold coins do you have? "))

#requires guests to be 18+ AND have 20+ gold coins
if GUEST_AGE >= 18 and NUMBER_OF_COINS >= 20:
    print("You may enter!")
else:
    print("You do not meet the requirements. You may not enter!")
