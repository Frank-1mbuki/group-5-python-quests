#Asks the user for their name and quest
def personalized_greeting():
    name=input("What is your name? ")
    quest=input("What is your quest? ")
    print(f"Welcome {name}! Your quest is: {quest}")

personalized_greeting()