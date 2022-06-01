# Program to make a Rock, Paper, Scissors game
# import random module
import random

# initial variables
possible_options = ["r", "p", "s"]
# set computer choice to random values from the 3 options
computer_choice = random.choice(possible_options)


while True:
    # take input from the user
    user_choice = input("Enter a choice with the initial letter of the following options:\n(Rock, Paper, Scissors): ").lower()
    
    # check if user input is valid
    if user_choice not in possible_options:
       user_choice = input("Invalid input. Please try again: ").lower()

    # display the choices made by the user and CPU players
    print(f"\n User Player ({user_choice.upper()}): CPU Player ({computer_choice.upper()})\n")

    # check if it is a tie
    while user_choice == computer_choice:
            
            print(f"Both User Player and CPU Player selected {user_choice.upper()}. \n It is a tie!")
            user_choice = input("Please try again: ").lower()
            computer_choice = random.choice(possible_options)

            print(f"\n User Player ({user_choice.upper()}): CPU Player ({computer_choice.upper()})\n")
    

    # decide the winner from the two players
    else:
        if user_choice == "r":
            if computer_choice == "s":
                print("User Player wins.")
                break
            else:
                print("CPU Player wins.")
                break
        elif user_choice == "p":
            if computer_choice == "r":
                print("PUser layer wins.")
                break
            else:
                print("CPU Player wins.")
                break
        elif user_choice == "s":
            if computer_choice == "p":
                print("User Player wins.")
                break
            else:
                print("CPU Player wins.")
                break