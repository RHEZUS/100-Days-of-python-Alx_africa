#!/usr/bin/python3
from functions import *

command = ''
while command != 'off':
    command = get_command()
    if command == 'off':
        exit()
    if command == 'report':
        print_report(stock)
        continue
    if not is_available(recipe[command], stock):
        continue
    coins = get_coins(recipe[command]['Price'])

    if not make_transaction(recipe[command]['Price'], coins):
        continue
    if make_coffee(command):
        print("Done! Good appetite")
