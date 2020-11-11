#!/usr/bin/python3

#                               PYTHON - USER INPUT AND LOOP

# Input function

# python2.7 raw_input("Tell me something:  ")
message = input("Tell me Something:  ")
print(message)

# Multiline Prompt

prompt = "If you tell me us who you are"
prompt += "\nWhat is you first name:  " 

name = input(prompt)

# Numerical 

age = input("Enter your age:  ")
print(int(age))

# While loop

current = 1
while(current <= 5):
    print(current)
    current += 1

# Quit on while loop
prompt = "Tell me something.  "
prompt += "Enter quit to Quit :) :  "

message = " " 
while(message != "quit"):
    message = input(prompt)
    print(message)


# Quit without boolean

while True:
    city = input("Tell me your favorite city: ")

    if city == 'quit':
        break;
    else: print("I love " + city)

# Continue ine while loop 1-3-5-7-9

current = 0

while current < 10:
    current += 1
    if current %2 == 0:
        continue

    print (current)

# While loop with dictionnary and list 

unconfirmed_users = ['alice','brian','candice']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user)
    confirmed_users.append(current_user)

print("\nThe following user has been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Remove all instances of specific value
pets = ['dog','cat','goldfish','cat','rabbit','cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling the dictionnary with user input

responses = {}

""" Set a flag to indicate that polling is active """
polling_active = True

while polling_active:
        name = input("Name: ")
        response = input("Last Name: " )

        responses[name] = response
        repeat = input("let another person respond(Yes/No) ")
        if repeat == 'no':
             polling_active = False

""" Polling is complete. Show the result """ 
print(" --- Polling Result ---")
for name,response in responses.items():
     print(name + "\tLast_Name: " + response)

     



