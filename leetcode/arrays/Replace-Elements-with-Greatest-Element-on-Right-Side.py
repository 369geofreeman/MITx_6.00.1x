# Replace Elements with Greatest Element on Right Side


# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# 
# After doing so, return the array.
# 
#  
# 
# Example 1:
# 
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#  
# 
# Constraints:
# 
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5


def replaceElements(arr):
    index = len(arr)-1
    unit = -1
    c = 0

    while index>-1:
        c = arr[index]
        arr[index] = unit
        if c>unit: unit=c
        index-=1
    return arr


print(replaceElements([17,18,5,4,6,1]))
# >>> [18,6,6,6,1,-1]



# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 128 ms
# Memory Usage: 14.8 MB
