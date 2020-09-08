# Plus One

# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# 
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# 
#  
# 
# Example 1:
# 
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
# 
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Example 3:
# 
# Input: digits = [0]
# Output: [1]
#


def plusOne(digits):
    if digits[-1] == 9:
        num = int(''.join(map(str,digits)))
        num += 1
        digits = list(map(int, str(num)))
    else:
        digits[-1] += 1
    return digits


print(plusOne([1, 2, 3]))
#  >>> [1, 2, 4]
print(plusOne([4, 3, 2, 1]))
#  >>> [4, 3, 2, 2]
print(plusOne([9, 9, 9, 9]))
# >>> [1, 0, 0, 0, 0]



# 109 / 109 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 13.7 MB
