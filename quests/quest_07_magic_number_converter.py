#!/usr/bin/env python3

from datetime import datetime

# Prompt user for input (birth year) and cast to integer.
birth_year = int(input("What is your birth year? "))

current_year = datetime.now().year

# Calculate the user's age
user_age = current_year - birth_year
print(f"You are {user_age} years old.")
