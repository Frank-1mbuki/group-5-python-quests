#!/usr/bin/python3

def main():
    number_1, number_2 = user_input()
    results = operations(number_1, number_2)
    print(results)
    
def user_input():
   number_1 = int(input("Enter the first number: "))
   number_2 = int(input("Enter the second number: "))
   return number_1, number_2

def operations(number_1, number_2):
    operand = input("Enter your operand: ")
    if operand == "+":
        return number_1 + number_2
    elif operand == "-":
        return number_1 - number_2
    elif operand == "*":
        return number_1 * number_2
    elif operand == "/":
        return number_1 / number_2
    elif operand == "%":
        return number_1 % number_2
    elif operand == "^":
        return number_1 ** number_2
    else:
        return "Invalid input"
        
main()
