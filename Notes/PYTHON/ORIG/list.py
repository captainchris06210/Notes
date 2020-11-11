#!/usr/bin/python3

"""                                     PYTHON  - LIST -                                 """


bicycles = [ 'Trek', 'Cannondale', 'Redline', 'Specialized' ]

""" Show element  """

print (bicycles[0])

""" To access at the last element in a list """

print (bicycles[-1])

""" Concatenation with string  - title add caps to the first letter """ 

msg = "My first bike was a " + bicycles[0].title() + "."

""" Changing the value of the first element """

bicycles[0] = "Sunn"

""" Inserting a new item to the end of the list """

bicycles.append('YT')

""" Inserting elements to N position """

bicycles.insert(1,'Morewood')

""" Remove the last item using the pop method """

popped_bicycle = bicycles.pop()
print(popped_bicycle)
""" Remove item by value  """

bicycles.remove('Redline')

""" Sort a list """

bicycles.sort()

""" Sort temporarily with sorted function """

print(sorted(bicycles))

""" length of a list """

print(len(bicycles))

""" List in loop """

for items in bicycles:
    print(items)

""" Create number list """ 

numbers = list(range(0,10))

""" min / max / sum """

print(sum(numbers))

""" Slice list """

print(numbers[0:3])

""" Looping a slice """

players =['charles', 'martina', 'michael', 'florence','eli']

for player in players[:3]:
    print(player.title())

""" Copying a list """ 

newList = players[:]

""" Define a tupple """

dimensions = (100,50)
print(dimensions[0])
print(dimensions[1])


