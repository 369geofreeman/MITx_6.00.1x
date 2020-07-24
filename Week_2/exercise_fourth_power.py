# Exercise: fourth power


# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.
# You should use the square procedure that you defined in an earlier exercise
# (you don't need to redefine square in this box; when you call square, the grader will use our definition).
# This function takes in one number and returns one number.

# Code Editor
# 1
# def fourthPower(x):


def square(x):
    # Your code here
    return x*x


def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(x) * square(x)


print(fourthPower(2))
