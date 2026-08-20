#!/usr/bin/python3

i = 0
code = "42"
while i < 3:
    secret_code = input("Enter the code: ")
    if secret_code == code:
        print("correct guess")
        break
    else:
        print("try again")
    i += 1
if i == 3:
    print("Failed attempts")
