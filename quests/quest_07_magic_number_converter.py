#!/usr/bin/env python3
# Prompt user for input and cast to integer.
birth_year=int(input("What is your birth year? "))

from datetime import datetime
current_year=datetime.now().year
#Calculate the users age
user_age=current_year-birth_year
print(f"{user_age}")
