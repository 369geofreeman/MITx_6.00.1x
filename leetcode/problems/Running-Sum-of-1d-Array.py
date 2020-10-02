# Running-Sum-of-1d-Array


# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# 
# Return the running sum of nums.
# 
# 
# 
# Example 1:
# 
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
# 
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
# 
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]



def runningSum(self, nums: List[int]) -> List[int]:
    s = 0
    res = []
    for i in nums:
        s+=i
        res.append(s)
    return res






# Runtime: 60 ms, faster than 18.27% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.3 MB, less than 5.05% of Python3 online submissions for Running Sum of 1d Array.


# 53 / 53 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 14.3 MB
