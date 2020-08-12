# Move Zeroes




# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.



def moveZeroes(arr):
    arrLen = len(arr)-1
    index = 0
    count = len(arr)

    while count!=0:
        if arr[index] == 0:
            arr.append(0)
            del arr[index]
        else:
            index+=1
        count-=1
    return arr


print(moveZeroes([0,1,0,3,12]))
# >>> [1,3,12,0,0]
print(moveZeroes([0,0,1]))
# >>> [1,0,0]



# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Memory Usage: 15 MB
