#!/usr/bin/python3

import json

""" Save Data in files """ 
numbers = [2,3,5,7,11,13]
filename = 'file.json'

with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

""" Load JSON File """

with open(filename) as file_obj:
    n = json.load(file_obj)

print(n)

""" Saving and reading userInput data """
username = input("What is your name: ")

filename = 'file.json'

with open(filename,'w') as file_obj:
    json.dump(username,file_obj)
    print('Well remember you when you come back ' + username)

""" Read data saved before """
with open(filename) as file_obj:
    user = json.load(file_obj)
    print('Welcome back: ' + user)
  
