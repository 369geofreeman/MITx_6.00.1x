# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic  𝑎⋅𝑥2+𝑏⋅𝑥+𝑐 .
# This function takes in four numbers and returns a single number.


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return a*(x*x)+b*x+c


print(evalQuadratic(6.19, -3.96, -7.86, -9.46))
