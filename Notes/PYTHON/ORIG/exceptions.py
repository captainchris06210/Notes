#!/usr/bin/python3

"""                                EXCEPTIONS                                    """

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by ZERO")

""" Preventing crash """
print("[q to Quit] Give me two numbers: " )

while True:
    first_number = input("First Number:  ")
    if first_number == 'q':
        break;
    second_number = input("Second Number:  ")

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by ZERO")
    else:
        print(answer)

""" File not found error """ 
filename = "test.txt"

try:
    with open(filename) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist"
    print(msg)
else:
    # Count approximatelly number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file has " + str(num_words) + " words")
""" Analizing Text """
title = "Alice in wonderland"

""" split the string and show 'in' word """
print(title.split()[1]) 

""" Working with mutliple files """
def count_words(filename):
    """ Count approximatelly the number of word """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
            msg = "The file: " + filename + " does not exist."
            print(msg)
    else:
        """ Count word in file """ 
        words = contents.split()
        num_words = len(words)
        print("The file: " + filename + " count: " + str(num_words) + " words")

filenames = ['test.txt','py_digits.txt','alice.txt','programming_langage.txt']
for filename in filenames:
    count_words(filename)


