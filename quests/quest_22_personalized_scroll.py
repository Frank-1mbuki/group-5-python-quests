#!/usr/bin/env python3

# Asks the user for their name and quest and prints a message.


def personalized_greeting():
    name = input("What is your name? ")
    quest = input("What is your quest? ")
    print(f"Welcome {name}! Your quest is: {quest}")


personalized_greeting()
