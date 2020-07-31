# Speed Code#2 Array Madness


# Objective
# Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.
# 
# E.g.
# 
# array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3



def array_madness(a,b):
    squareSum = sum([x**2 for x in a])
    cubeSum = sum([x**3 for x in b])
    return squareSum > cubeSum

print(array_madness([4, 5, 6], [1, 2, 3]))
