#!/usr/bin/python3
print("")
print("Welcome to Treasure island.\nYour Mission is to find the Treasure")

value = input("You are at a cross road. Where do you want to go? type \"left\" or \"right\"\n")

while value not in ('left', 'right'):
    print("Error!: Your input must be \"left\" or \"right\"")
    value = input("You are at a cross road. Where do you want to go? type \"left\" or \"right\"\n")

if value == 'right':
    print("Game Over!")
    exit()

value = input("You are at a lake. there is an island in the middle of the lake. Type \"wait\" to wait for the boat or  \"swim\" to swim across\n")
while value not in ('wait', 'swim'):
    print("Error!: Your input must be \"wait\" or \"swim\"")
    value = input("You are at a lake. there is an island in the middle of the lake. Type \"wait\" to wait for the boat or  \"swim\" to swim across\n")

if value == 'swim':
    print("Game Over!")
    exit()

value = input("You are at the island unharmed. there is a house with three doors. One red, one yellow and one blue which color do you choose.\n")
while value not in ('red', 'yellow', 'blue'):
    print("Error!: Your input must be \"red\" or \"yellow\" or \"blue\"")
    value = input("You are at the island unharmed. there is a house with three doors. One red, one yellow and one blue which color do you choose.\n")

if value != 'Yellow':
    print("Game Over!")
    exit()
else:
    print("You win!")

