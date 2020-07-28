######## Example code blocks ########


# List comprehension

# you can itterate through multiple list simultansiously useing list comprehension as shown below where
# we print a list of all possible coordinates given by (z,x,y) and only return if they do not match the sum of n

x = 2
y = 2
z = 2
n = 2

print([[i, j, k] for i in range(x+1) for j in range(y+1)
       for k in range(z+1) if sum([i, j, k]) != n])


# to fixed number

print("{:.2f}".format(13.949999999999999))
# returns 13.94


### One line itteration ###

# one line if + loop
res = [l for l in s if l in v]

# One line if + else + loop
[l if l in lettersGuessed else '_' for l in secretWord]


### lambda function ###
# A lambda operator or lambda function is used for creating small, one-time, anonymous function objects in Python.
# lambda arguments : expression

# Example
def add(x, y):
    return x + y


add(2, 3)  # Output: 5


### Map ###
# map(function_object, iterable1, iterable2,...)

# Example
def multiply2(x):
    return x * 2


map(multiply2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]


# Map with lambda
map(lambda x: x*2, [1, 2, 3, 4])  # Output [2, 4, 6, 8]

# Iterating Over a Dictionary Using Map and Lambda
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

map(lambda x: x['name'], dict_a)  # Output: ['python', 'java']

map(lambda x: x['points']*10,  dict_a)  # Output: [100, 80]

map(lambda x: x['name'] == "python", dict_a)  # Output: [True, False]

# Multiple Iterables to the Map Function
# We can pass multiple sequences to the map functions as shown below:
list_a = [1, 2, 3]
list_b = [10, 20, 30]

map(lambda x, y: x + y, list_a, list_b)  # Output: [11, 22, 33]


### Filter ##


### Lambda with filter  ###

# Basic Syntax
# filter(function_object, iterable)

a = [1, 2, 3, 4, 5, 6]
filter(lambda x: x % 2 == 0, a)  # Output: [2, 4, 6]

# Filter ist of dicts
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

# Output: [{'name': 'python', 'points': 10}]
filter(lambda x: x['name'] == 'python', dict_a)

# Similar to map, the filter function in Python3 returns a filter object or the iterator which gets lazily evaluated.
# We cannot access the elements of the filter object with index, nor can we use len() to find the length of the filter object.


list_a = [1, 2, 3, 4, 5]

# filter object <filter at 0x4e45890>
filter_obj = filter(lambda x: x % 2 == 0, list_a)

even_num = list(filter_obj)  # Converts the filer obj to a list

print(even_num)  # Output: [2, 4]
