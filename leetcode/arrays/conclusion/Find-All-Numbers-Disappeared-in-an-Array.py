# Find All Numbers Disappeared in an Array




# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]




def findDisappearedNumbers(nums):
    return list(set([x for x in range(1, len(nums)+1)]) - set(nums))


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
# >>> [5,6]


# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 360 ms
# Memory Usage: 24.7 MB
