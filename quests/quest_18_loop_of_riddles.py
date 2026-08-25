#!/usr/bin/env python3
while True:
    secret_number=int(input("Guess a number between 0 and 10: " ))
    if secret_number==7:
        print("You nailed it!")
        break
    print("Nice try! Give it another go.")
