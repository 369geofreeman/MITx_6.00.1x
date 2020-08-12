# Number of Good Pairs

# Given an array of integers nums.
# 
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# 
# Return the number of good pairs.
# 
#  
# 
# Example 1:
# 
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:
# 
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:
# 
# Input: nums = [1,2,3]
# Output: 0

def numIdenticalPairs(nums):
        res = 0
        done = []
        for i in nums:
            x = nums.count(i)
            if x > 1 and i not in done:
                res += (x*(x-1)//2)
            done.append(i)
        return res


print(numIdenticalPairs([1,2,3,1,1,3]))



# 48 / 48 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.8 MB
