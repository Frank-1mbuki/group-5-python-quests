birth_year=int(input("What is your birth year? "))

from datetime import datetime
current_year=datetime.now().year

user_age=current_year-birth_year
print(f"{user_age}")