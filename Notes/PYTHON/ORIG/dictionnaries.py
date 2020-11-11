#!/usr/bin/python3

""" Declare dictionnaries """
alien_0 = {'color': 'green', 'points': 5 }

print("  Color:  " + alien_0['color'] + "  Points:  " +  str(alien_0['points']))

""" Remove value from dictionnary """
del alien_0['points']

favorite_langage = {
        'Paul' : 'Ruby', 'Henry' : 'Asm', 'Jen' : 'C++' 
        }

""" Loop in dictionnary """
for key,value in favorite_langage.items():
    print("Key: " + key + "\tValue: " + value)

""" Loop only key """
for key in favorite_langage.keys():
    print(key)

""" Loop only value """ 
for value in favorite_langage.values():
    print(value) 

""" Loop a dictionnary in order """
for l in sorted(favorite_langage.keys()):
    print(l + "\tThank you to taking the poll")

""" Create empty list and store value """ 
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = { 'color' : 'green', 'points' : '5', 'speed' : 'slow'}
    aliens.append(new_alien)

# Show the first five alien
for alien in aliens[:5]:
    print(alien)
    print("...")

# Show how many alien have been created
print("Total number of aliens: " + str(len(aliens)))

# List in a dictionnary
pizza = {
        'crust': 'thick',
        'toppings': ['musrooms','xtra cheese'],
        }

print("You ordered " + pizza['crust'] + "-crust pizza " + " with the following toppings: ")
for toppings in pizza['toppings']:
    print("\t" + toppings)

# dictionnary in dictionnary
users = {
        'aeinstein': {
            'first': 'Albert',
            'last': 'Einstein',
            'location':'princeton',
            },
        
        'mcurie': {
            'first': 'Marie',
            'last': 'Curie',
            'location': 'Paris',
            },
        }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last'] 
    location = user_info['location']

    print("\tFullName: " + full_name.title())
    print("\tLocation: " + location.title())

""" Ordered dictionnaries """
from collections import OrderedDict

favorites_langage = OrderedDict()

favorite_langage['Jen'] = 'Python'
favorite_langage['Sarah'] = 'C'
favorite_langage['Edward'] = 'Ruby'
favorite_langage['Phil'] = 'Python'
favorite_langage['Sarah'] = 'c'

for name, langage in favorite_langage.items():
    print(name.title() + "'s favorite langage is " + langage.title() + ".")


