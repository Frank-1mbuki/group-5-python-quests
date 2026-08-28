#!/usr/bin/env python3
#This script is a riddle that displays your results immidiately you give an answer
option = input("Hi! Are you going right or left? ")
if option == "left":
    option_2 = input("Will you swim or you will wait? ")
    if option_2 == "swim":
        print("Congratulations! You found a treasure")
    else:
        print("Try again")

else:
    print("Try again")
