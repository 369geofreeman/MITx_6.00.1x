# Duplicate Zeros



# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
# 
# Note that elements beyond the length of the original array are not written.
# 
# Do the above modifications to the input array in place, do not return anything from your function.
# 
# 
# 
# Example 1:
# 
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:
# 
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]
# 
# 
# Note:
# 
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9


def duplicateZeros(arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        c = 0
        l = len(arr)
        while(c<l):
            if arr[c] == 0:
                arr.insert(c,0)
                c+=2
                del arr[-1]
            else:
                c +=1
#        return arr <--- uncomment to test


print(duplicateZeros([1,0,2,3,0,4,5,0]))
print('expected result: {}'.format([1,0,0,2,3,0,0,4]))


# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 72 ms
# Memory Usage: 14.5 MB
