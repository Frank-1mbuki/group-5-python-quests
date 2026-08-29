#!/usr/bin/env python3

# Prompt the user for their age and convert the input string to an integer.
user_age = int(input("What is your age? "))

# Check if the user meets the legal voting age requirement (18 or older).
if user_age >= 18:
    print("You are old enough to vote")
else:
    print("You may not pass! You are too young to vote.")
