# Grader: Regular Polygon


# A regular polygon has n number of sides. Each side has length s.

# The area of a regular polygon is:  0.25∗𝑛∗𝑠2𝑡𝑎𝑛(𝜋/𝑛)
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.


import math


def polysum(n, s):
    area = (0.25*n*(pow(s, 2))) / (math.tan(math.pi/n))
    square = (n*s)**2
    return round((area + square), 4)


print(polysum(82, 39))


# Test: polysum(82, 39)
# Your output:
# 813456.7995

# Correct output:
# 11040660.7995
