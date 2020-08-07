# Greatest Common Divisor
# ---

# Euclid’s Algorithm states that the greatest common divisor of two integers 𝑚 and 𝑛 is 𝑛 if 𝑛 divides 𝑚 evenly. However, if 𝑛 does not divide 𝑚 evenly, then the answer is the greatest common divisor of 𝑛 and the remainder of 𝑚 divided by 𝑛


def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

print(gcd(20,10))
