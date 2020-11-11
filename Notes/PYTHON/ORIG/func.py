#!/usr/bin/python3 

#                                           PYTHON - FUNCTIONS                                                       #

# Defining a function 

def greet_user():
    print("Hello")

# Defining function with default value

def describe_pet(pet_name,animal_type='dog'):
    print("Animal: " + animal_type,"\t Name: " + pet_name)

describe_pet(pet_name='harry')

# Return a value

def get_formatted_name(first_name, last_name):
    full_name = first_name + last_name
    return full_name.title()

print(get_formatted_name('jimi ',' hendrix'))

# Return dictionnary

def build_person(first_name,last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)

# Function in a while loop

while True:
    f_name = input("first Name: " )
    l_name = input("last_name: ")

    formated_name = get_formatted_name(f_name,l_name)
    print(formated_name)
    if f_name == 'q' or l_name =='q' :
        break
   
# Passing a list to a function

def greet_users(names):
    for name in names:
        msg = "Hello " + name.title() + "!"
        print (msg)

usernames =['hannah','ty','margot']
greet_users(usernames)

# Send a copy of list 

#function_name(list_name[:])

# Passing an arbritary number of arguments (* Create an empty tupple to store information)

def make_pizza(*toppings):
    for topping in toppings:
        print("- " + topping)

make_pizza('peperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# Mixing positional and arbritary arguments

def make_pizza(size,*toppings):
    for topping in toppings:
        print("Pizza size : " + str(size) + "\t Toppings: " + topping)


make_pizza(12,'peperoni')
make_pizza(16,'mushrooms','green peppers','extra cheese')

# Using arbitary keyword argument (** Create a dictionary)

def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key ,value in user_info.items():
        profile[key] = value

    return profile 

user_profile = build_profile('albert','einstein',
        location='princeton',
        field='physics')

print(user_profile)

# Import func from module - pizza.py
            
        # FILE: pizza.py

def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) +" inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

       # FILE: import pizza

pizza.make_pizza(16,'peperroni')

# Importing specific Functions Example: from module_name import func0, func1, func2

from pizza import make_pizza
make_pizza(16,'mushroom')

# import Alias function

from pizza import make_pizza as mp
mp(16,'peperroni')

# Alias of module

import pizza as p
p.make_pizza(16,'peperonni')

# Import all function from module

from pizza immport *

# PEP 8 recommendation 79 char by line
def func_name (
        parameter 0, parameter 1, 
        parameter 3, parameter 4):
    func_body

