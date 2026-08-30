#!/usr/bin/python3
#this ask the user to enter a score and ccompares it and then prints a grade
score = float(input("Enter your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")
