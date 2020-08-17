# Create Target Array in the Given Order


# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
# 
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
# 
# It is guaranteed that the insertion operations will be valid.
# 
#  
# 
# Example 1:
# 
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]
# Example 2:
# 
# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# Explanation:
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]
# Example 3:
# 
# Input: nums = [1], index = [0]
# Output: [1]



def createTargetArray(nums, index):
    res = []
    for i,v in enumerate(index):
        res.insert(v,nums[i])
    return res



print(createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
# >>> [0,4,1,3,2]
print(createTargetArray([1,2,3,4,0],[0,1,2,3,0]))
# >>> [0,1,2,3,4]
print(createTargetArray([1],[0]))
# >>>> [1]



# 44 / 44 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.8 MB



