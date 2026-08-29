#!/usr/bin/env python3

# Loop continuously until the user guesses the correct number.
while True:
    secret_number = int(input("Guess a number between 0 and 10: "))
    
    # Exit the loop immediately if the winning condition is met.
    if secret_number == 7:
        print("You nailed it!")
        break
        
    # Provide feedback for incorrect guesses before looping again.
    print("Nice try! Give it another go.")
