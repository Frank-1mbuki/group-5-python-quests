#!/usr/bin/env python3

guest_age = int(input("How old are you? "))
number_of_coins = int(input("How many gold coins do you have? "))

# Requires guests to be 18+ AND have 20+ gold coins
if guest_age >= 18 and number_of_coins >= 20:
    print("You may enter!")
else:
    print("You do not meet the requirements. You may not enter!")
    
