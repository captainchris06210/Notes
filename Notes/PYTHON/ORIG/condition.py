#!/bin/python3

cars =['Audi', 'BMW', 'Subaru', 'Toyota']

for car in cars:
    if car == 'BMW':
        print(car.upper())

""" Check Inequality """
if cars != 'Nissan':
    print("No Toy")

""" Test Multiple conditions """
age = 16

if (age > 0 and age >= 21):
    print("The age is in the range")

""" Checking in the list """
requested_toppings = ['mushrooms','onions','pineaple']

if('mushrooms' in requested_toppings):
    print("They are mushrooms in recipe")

""" Checking if a vlaue is not in a list """
if ('pepperoni' not in requested_toppings):
    print("No pepperoni in recipe")

""" if / else condition """ 
age = 17

if age >= 18:
    print("You are old enought to vote")
else: 
    print("Sorry, you are too young to vote")
   
""" if / elif / else """
age = 12

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

""" Checking in the list """
requested_toppings = ['mushrooms','green_peppers','extra_cheese']
for requested_toppings in requested_toppings:
    print("Adding  " + requested_toppings)

print ("Pizza Finished")

""" Using multiple lists """
available_toppings = ['mushrooms','green_peppers','extra_cheese']
requested_toppings = ['mushrooms','french fries','extra_cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry,we don't have " + requested_topping + ".")

print("\nFinished makiing your pizza")

