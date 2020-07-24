# Exercise: gcd iter


# The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

# gcd(2, 12) = 2

# gcd(6, 12) = 6

# gcd(9, 12) = 3

# gcd(17, 12) = 1

# Write an iterative function, gcdIter(a, b), that implements this idea.
# One easy way to do this is to begin with a test value equal to the smaller of the two input arguments,
# and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.

# Loop version
def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    loop = a if a < b else b
    while a != 0:
        if a % loop == 0 and b % loop == 0:
            return loop
        a -= 1
    return loop


print('Loop version: ', end='')
print(gcdIter(6, 12))


# Recursive version

# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:
# If b = 0, then the answer is a
# Otherwise, gcd(a, b) is the same as gcd(b, a % b

def gcdRecu(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    return gcdRecu(b, a % b)


print('Recursive version: ', end='')
print(gcdRecu(9, 12))
