# Project: Creating Snake, Water, Gun Game (For rules, refer to the Readme file)

import random # Import random module

def game():
    
    # Generate a random number between 1 and 3 for the computer's choice (using random module)
    random_num = random.randint(1, 3)
    computer = random_num

    # Define the objects dictionary
    objects = {1 : "Snake", 2 : "Water", 3 : "Gun"}

    # Print the options for the player and take input
    player = int(input("Make your choice:\nPress 1 - Snake\nPress 2 - Water\nPress 3 - Gun\nEnter your choice: "))

    # Check if the game is a draw
    if computer == player:
        print(f"\nGame is draw! You both chose {objects[player]}")

    # Check for other game outcomes
    elif (computer==1) and (player==2):
        print(f"\nYou lost! Opponent's {objects[1]} drank your {objects[2]}.")
    elif (computer==2) and (player==1):
        print(f"\nYou win! Your {objects[1]} drank Opponent's {objects[2]}.")
    elif (computer==1) and (player==3):
        print(f"\nYou win! Your {objects[3]} shot Opponent's {objects[1]}.")
    elif (computer==3) and (player==1):
        print(f"\nYou lost! Opponent's {objects[3]} shot your {objects[1]}.")
    elif (computer==3) and (player==2):
        print(f"\nYou win! Opponent's {objects[3]} sunk in your {objects[2]}.")
    elif (computer==2) and (player==3):
        print(f"\nYou lost! Your {objects[3]} sunk in Opponent's {objects[2]}.")
    else:
        print("\nInvalid choice, Please enter 1, 2, or 3.")

# Create Game's Main Welcome Screen and Menu

# Create game menu using loop
while True:
    print('''\n*** Welcome back to the SNAKE, WATER, GUN Game ***\n\nWhat would you like to do?''')
    choice = int(input("\nPress 1 for New Game\nPress 2 to Exit the Game\n\nEnter your choice: "))

    if choice==1:
        print("\nLet's Play.....\n")
        game()
    elif choice==2:
        print("\nQuitting the Game.....")
        break
    elif (choice>2) or (choice<1):
        print("\nInvalid choice, enter number 1 or 2.")