# Valid Mountain Array

# Given an array A of integers, return true if and only if it is a valid mountain array.
# 
# Recall that A is a mountain array if and only if:
# 
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
# 
# 
#  
# 
# Example 1:
# 
# Input: [2,1]
# Output: false
# Example 2:
# 
# Input: [3,5,5]
# Output: false
# Example 3:
# 
# Input: [0,3,2,1]
# Output: true
#  
# 
# Note:
# 
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000 


def validMountainArray(arr):
        if len(arr)<3: return False
        k = arr[0]
        index = 0

        for i in range(1,len(arr)):
            if arr[i]<=k:
                index = i
                break
            k = arr[i]
        if index == len(arr): return False
        if index<=1: return False

        for i in range(index,len(arr)):
            if arr[i]>=k:
                return False
            k = arr[i]
        return True



print(validMountainArray([9,8,7,6,5,4,3,2,1,0]))
print(validMountainArray([1,3,2]))
print(validMountainArray([0,3,2,1]))




# 51 / 51 test cases passed.
# Status: Accepted
# Runtime: 200 ms
# Memory Usage: 15 MB
