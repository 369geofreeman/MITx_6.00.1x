# coding=utf-8

# what's your name?

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.


x = 'Brian'
y = 'Jones'

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))


print(print_full_name(x, y))
