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

    while index<len(A):
        if A[index] %2==0:
            A.append(A[index])
            del A[index]
        else:
            index+=1




print(sortArrayByParity([3,1,2,4]))
# >>> [2,4,3,1],[4,2,3,1],[2,4,1,3], or [4,2,1,3]
