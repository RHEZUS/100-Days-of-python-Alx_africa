stock = {'Water': 2000, 'Milk': 1000, 'Coffee': 700, 'Money': 0}
recipe = {
    'espresso':{'Water': 40, 'Milk': 0, 'Coffee': 20, 'price': 2},
    'latte':{'Water': 30, 'Milk': 35, 'Coffee': 40, 'Price': 3},
    'cappuccino':{'Water': 30, 'Milk': 45, 'Coffee': 40, 'Price': 4}
}

def get_command():
    command_list = ('espresso', 'latte', 'cappuccino', 'off', 'report')
    command = input("What would you like? (espresso/latte/cappuccino): ")
    while command not in command_list:
        print("Sorry we only have (espresso/latte/cappuccino)")
        command = input("What would you like? (espresso/latte/cappuccino): ")
    return(command)

def print_report(stock):
    for item in stock.keys():
        if item in ('Water', 'Milk'):
            print("{}: {}ml".format(item, stock[item]))
        elif item == 'Coffee':
            print("{}: {}g".format(item, stock[item]))
        else:
            print("{}: ${}".format(item, stock[item]))

def is_available(command, stock):
    if command['Water'] > stock['Water']:
        print("Sorry there is not enough water.")
        return(0)
    elif command['Milk'] > stock['Milk']:
        print("Sorry there is not enough water.")
        return(0)
    elif command['Coffee'] > stock['Coffee']:
        print("Sorry there is not enough water.")
        return(0)
    return(1)

def get_coins(price):
    value = input("insert coins: ")
    coins = float(value)
    while value != 'stop' and coins < price:
        value =  input("insert coins (${}): ".format(price))
        coins += float(value)
    return coins

def make_transaction(price, coins):
    if coins < price:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif coins > price:
        stock['Money'] += price
        print("Here is ${:.2f} dollars in change.".format(coins - price))
        return 1
    else:
        stock['Money'] += coins
        print("Transaction successful.")
        return 1

def make_coffee(command):
    stock['Water'] -= recipe[command]['Water']
    stock['Milk'] -= recipe[command]['Milk']
    stock['Coffee'] -= recipe[command]['Coffee']
    return 1