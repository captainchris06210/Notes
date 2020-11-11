#!/usr/bin/python3

""" Open with absolute path """
filepath = '/home/captainchris/Work/Python/Learning/py_digits.txt'

with open(filepath) as file_object:
    content = file_object.read()
    
    """ rstrip() remove space after string and newlinecharacter (\n) """
    print(content.rstrip())

""" Open directly """
with open('py_digits.txt') as file_object:
    content = file_object.read()
    print(content)


""" Read line by line """
i = 0

with open('py_digits.txt') as file_object:
    for line in file_object:
        print(str(i) + ":" + line.rstrip())
        i += 1

""" Making a list of lines from file """
filename = 'py_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ' '

for line in lines:
    pi_string = line.rstrip()

""" Is your birthday contained in pi string """
filename = 'pi_million_digits.txt'

with open(filename) as fileobject:
    lines = fileobject.readlines()

pi_string = ' '

for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter you birthday[mmddyy]: ")

if birthday in pi_string:
    print("Your birthday appears in pi million digits")
else:
    print("Your birthday does not appear in pi million digits")
    

""" Writting to a file """ 
file = 'programming_langage.txt'

""" w : write a: append """
with open(file, 'a') as file_object:
    file_object.write("I Love Programming")
    file_object.write("I Love Computer")

