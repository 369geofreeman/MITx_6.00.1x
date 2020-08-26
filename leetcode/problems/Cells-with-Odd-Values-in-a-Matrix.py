# Cells with Odd Values in a Matrix


# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.
# 
# Return the number of cells with odd values in the matrix after applying the increment to all indices.
# 
#  
# 
# Example 1:
# 
# 
# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
# Example 2:
# 
# 
# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.


def oddCells(n,m,indices):
    yy=set()
    xx=set()
    for y,x in indices:
        if y in yy:yy.remove(y)
        else:yy.add(y)
        if x in xx:xx.remove(x)
        else:xx.add(x)
    a=len(yy)
    b=len(xx)
    return a*(m-b)+b*(n-a)

print(oddCells(2,3,[[0,1],[1,1]]))
# >>> 6
# print(oddCells(2,2,[[1,1],[0,0]]))
# >>> 0


# Runtime: 40 ms, faster than 92.36% of Python3 online submissions for Cells with Odd Values in a Matrix.
# Memory Usage: 14.1 MB, less than 17.64% of Python3 online submissions for Cells with Odd Values in a Matrix.


# 44 / 44 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 14.1 MB
