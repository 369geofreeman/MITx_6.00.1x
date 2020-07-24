# Exercise: power iter

# Write an iterative function iterPower(base, exp) that calculates the exponential  baseexp  by simply using successive multiplication.
# For example, iterPower(base, exp) should compute  baseexp  by multiplying base times itself exp times. Write such a function below.

# This function should take in two values - base can be a float or an integer; exp will be an integer  ≥  0.
# It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.

import random


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1.0
    res = base
    while exp > 1:
        res *= base
        exp -= 1
    return res


# Tests
for x in range(10):
    base = random.randint(0, 100)
    exp = random.randint(0, 5)
    print(iterPower(base, exp))
