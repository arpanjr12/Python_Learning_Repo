'''
create a stone,paper,scissor game 
'''
# Stone vs paper => paper wins.
# stone vs scissor Gun => stone wins.
# scissor vs paper => scissor wins.

import random 

def choice():
    return random.choice(["Stone", "Paper", "Scissor"])

def game_winner(player, computer):  

    if player == computer:
        return "It's a Draw!"
    elif (player == "Paper" and computer == "Stone") or \
         (player == "Scissor" and computer == "Paper") or \
         (player == "Stone" and computer == "Scissor"):

        return "You Won"
    else:
        return "Computer Won"

print("Welcome to Stone-Paper-Scissor!\n Choose between Stone, Paper, Scissor:")

while True:       
   
    Your_choice = input("Enter your choice (or 'exit' to quit): ").capitalize()
    
    if Your_choice == "Exit":
        print("Thanks for playing!")
        break

    if Your_choice not in ["Stone", "Paper", "Scissor"]:
        print("Invalid choice! Please choose between the given options.")
        continue

    computer_choice = choice()
    print(f"Computer chose: {computer_choice}")

    result = game_winner(Your_choice, computer_choice)  
    print(result)
    print()  




