'''
We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user
'''
# Snake drinks Water => Snake wins.
# Water douses Gun => Water wins.
# Gun kills Snake => Gun wins.

import random

def choice():
    return random.choice(["Snake", "Water", "Gun"])

def winner(player, computer):
    
    if player == computer:
        return "It's a draw!"
    
    elif player == "Snake" and computer == "Water" or \
         player == "Water" and computer == "Gun" or \
        player == "Gun" and computer == "Snake":
        return "You win!"
    else:
        return "Computer wins!"


print("Welcome to Snake-Water-Gun Game!  Choices between Snake, Water, Gun: ")


while True:        #~~~~~"while True" would create an infinite loop that only stops when the program is  closed.
    

    player_choice = input("Enter your choice (or 'exit' to quit): ").capitalize()
    
    if (player_choice == "Exit") :
        print("Thanks for playing!")
        break

    if player_choice not in ["Snake", "Water", "Gun"]:
        print("Invalid choice! Please choose between  Snake, Water, or Gun.")
        continue

    computer_choice = choice()
    print(f"Computer chose: {computer_choice}")

    result = winner(player_choice, computer_choice)
    print(result)
    print()  

