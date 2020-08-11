# Squares of a Sorted Array

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
# 
#  
# 
# Example 1:
# 
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:
# 
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#  
# 
# Note:
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.


def sortedSquares(A):
#    return sorted([i**2 for i in A])
    res = []
    for i in A:
        r = i**2
        res.append(r)
    res.sort()
    return res


print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))


# 132 / 132 test cases passed.
# Status: Accepted
# Runtime: 228 ms
# Memory Usage: 15.6 MB
