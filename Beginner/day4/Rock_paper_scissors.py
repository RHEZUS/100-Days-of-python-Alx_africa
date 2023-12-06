#!/usr/bin/python3
import random
from game_images import *

game_images = [rock, paper, scissors]
User_input = input("What do you choose? type 0 for Rock, 1 for paper and 2 for Scissors: ")
choices = ['Rock', 'Paper', 'Scissors']

if User_input not in ('0', '1', '2'):
    print("Wrong Input! You loose.")
else:
    User_input = int(User_input)
    print("Your choice: {} \n {}".format(choices[User_input], game_images[User_input]))
    computer_input = random.randint(0, 2)
    print("Computer's choice: {} \n {}".format(choices[computer_input], game_images[computer_input]))

    if computer_input == 2 and User_input == 0:
        print("You win!")
    elif computer_input == 0 and User_input == 2:
        print("You Loose!")
    elif  computer_input > User_input:
        print("You Loose!")
    elif User_input > computer_input:
        print("You win!")
    elif User_input == computer_input:
        print("It's a draw!")


