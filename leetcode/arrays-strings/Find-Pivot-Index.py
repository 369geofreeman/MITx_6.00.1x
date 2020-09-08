# FInd Pivot Index

# Given an array of integers nums, write a method that returns the "pivot" index of this array.
#
# We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.
#
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
#
#
#
# Example 1:
#
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# Example 2:
#
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.


def pivotIndex(nums):
    if len(nums) == 0: return -1
    for i in range(len(nums)+1):
        if i > 1 and sum(nums[0:i-1]) == sum(nums[i:len(nums)]):
            return i-1
        elif i == 0 and sum(nums[1:]) == 0:
            return 0
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
#  >>> 3
print(pivotIndex([1, 2, 3]))
#  >>> -1
print(pivotIndex([-1, -1, -1, -1, -1, 0]))
#  >>> 2
print(pivotIndex([-1, -1, -1, 0, 1, 1]))
#  >>> 0
print(pivotIndex([-1, -1, 0, 1, 1, 0]))
#  >>> 5

#  Runtime: 9396 ms, faster than 5.02% of Python3 online submissions for Find Pivot Index.
#  Memory Usage: 14.8 MB, less than 91.74% of Python3 online submissions for Find Pivot Index.


# 742 / 742 test cases passed.
# Status: Accepted
# Runtime: 9640 ms
# Memory Usage: 15 MB
