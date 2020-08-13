# Sort Array By Parity


# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
#  
# 
# Example 1:
# 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.



def sortArrayByParity(A):
    index = 0
    count = 0

    while count<len(A):
        if A[index] %2!=0:
            A.append(A[index])
            del A[index]
        else:
            index+=1
        count+=1
    return A




print(sortArrayByParity([3,1,2,4]))
# >>> [2,4,3,1],[4,2,3,1],[2,4,1,3], or [4,2,1,3]

# 285 / 285 test cases passed.
# Status: Accepted
# Runtime: 84 ms
# Memory Usage: 14.2 MB
