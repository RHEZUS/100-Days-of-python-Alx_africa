#!/usr/bin/python3
print("welcome to the tip calculator")

total = float(input("What was the total of the bill? $"))
while total < 0:
    print("Error: Please enter a value grater than 0")
    total = float(input("What was the total of the bill? $"))

tip = float(input("what percentage tip would you like to give? 10, 12 or 15?"))
while tip not in (10, 12, 15):
    print("Error: The tip should be 10, 12 or 15 %")
    tip = float(input("what percentage tip would you like to give? 10, 12 or 15?"))

payer = int(input("How many people will split the bill? "))
while payer < 0:
    print("Error: Please enter a value grater than 0")
    payer = int(input("How many people will split the bill? "))

pay = (total + (total * tip) / 100) / payer
print("each person should pay: {:.2f}".format(pay))
