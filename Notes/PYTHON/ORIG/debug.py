#!/usr/bin/python3

import unittext
from ext import get_formatted_name

print('Enter q to quit')

while True:
    first = input('\nPlease give me your first name: ')
    if first == 'q':
        break
    last = input('\nGive me your last name: ')
        
    formatted_name = get_formatted_name(first,last)
    print('\nNeatly formatted name:' + formatted_name + '.')

 
