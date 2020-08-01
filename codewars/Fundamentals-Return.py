# Fundamentals: Return

# Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.
# 
# Please use the following function names:
# 
# addition = add
# 
# multiply = multiply
# 
# division = divide (both integer and float divisions are accepted)
# 
# modulus = mod
# 
# exponential = exponent
# 
# subtraction = subt
# 
# Note: All math operations will be: a (operation) b


import math

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a//b

def mod(a,b):
    return math.fmod(a, b)

def exponent(a,b):
    return a**b

def subt(a,b):
    return a-b




