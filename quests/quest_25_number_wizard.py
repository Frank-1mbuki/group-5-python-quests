#!/usr/bin/env python3
while True:
    guessed_number = input("Guess a number(0-100): ")
    if guessed_number.isdigit():
        guessed_number = int(guessed_number)
        # 47 is the real number
        difference = 47 - guessed_number
        if difference > 0:
            print("Too low!")
        elif difference < 0:
            print("Too high!")
        else:
            print("Correct!")
            break
    else:
        print("Invalid input. Please enter numbers only 0 to 100.")