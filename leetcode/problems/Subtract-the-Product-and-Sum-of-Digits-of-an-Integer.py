# Subtract the Product and Sum of Digits of an Integer


# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
#  
# 
# Example 1:
# 
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# Example 2:
# 
# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21


def subtractProductAndSum(n):
    s,m = 0,1
    for i in str(n):
       s+=int(i)
       m*=int(i)
    return m-s




print(subtractProductAndSum(234))
# >>> 15



# 123 / 123 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.6 MB
