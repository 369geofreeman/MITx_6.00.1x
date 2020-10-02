# Spiral Matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# 
# Example 1:
# 
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
# 
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return []
        i,j,di,dj = 0,0,0,1
        m, n = len(matrix),len(matrix[0])
        for v in range(m * n):
            res.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i+di)%m][(j+dj)%n] == '':
                di, dj = dj, -di
            i += di
            j += dj
        return res






# 22 / 22 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 14.2 MB
