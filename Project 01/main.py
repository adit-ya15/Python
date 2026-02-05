# import random

# choice = ["Water","Gun","Snake"]

# print(''' 
# Entering In The Game of Snake, Water and Gun...🐍💦🔫

# Game Rules
# Snake vs. Water: Snake wins (drinks the water).
# Water vs. Gun: Water wins (gun sinks/drowns).
# Gun vs. Snake: Gun wins (shoots the snake).
# Same Choice: If both players choose the same object, the match is a draw. 
# ''')

# def game(choice):
#     computer = random.choice(choice)
#     user = input("Enter your call: ")

#     if(computer == user):
#         print("It's Draw 📍📍")
#         return game(choice)
#     elif(computer == "Snake" and user == "Water"):
#         print("Computer Wins 😒😒")
#     elif(computer == "Water" and user == "Gun"):
#         print("Computer Wins 😒😒")
#     elif(computer == "Gun" and user == "Snake"):
#         print("Computer Wins 😒😒")
#     else:
#         print("You Win 😎😎")

# game(choice)

#IMPROVEMENT IN ABOVE CODE
# Always remember that not use recursion in game
# No input validation
# Case-sensitive bug 

import random

choices = ["Water", "Gun", "Snake"]

print("""
Entering The Game of Snake, Water and Gun... 🐍💦🔫

Rules:
Snake beats Water
Water beats Gun
Gun beats Snake
Same choice = Draw
""")

while True:
    computer = random.choice(choices)
    user = input("Enter your call (Water/Gun/Snake): ").capitalize()

    if user not in choices:
        print("Invalid choice ❌ Try again.\n")
        continue

    print(f"Computer chose: {computer}")

    if computer == user:
        print("It's a Draw 📍📍\n")
    elif (
        (computer == "Snake" and user == "Water") or
        (computer == "Water" and user == "Gun") or
        (computer == "Gun" and user == "Snake")
    ):
        print("Computer Wins 😒😒\n")
        break
    else:
        print("You Win 😎😎\n")
        break
