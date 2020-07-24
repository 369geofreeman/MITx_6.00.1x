# Exercise: odd

# Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.
# You should use the % (mod) operator, not if.
# This function takes in one number and returns a boolean.

import random


def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x % 2 != 0


# Tests
for x in range(10):
    num = random.randint(0, 100)
    print(odd(num))
