# Diagonal Traverse


# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
#
#
#
# Example:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]


def findDiagonalOrder(matrix):
    if not matrix and not matrix[0]: return []

    rl, cl = len(matrix), len(matrix[0])
    res = []
    row, col = 0, 0

    while row < rl and col < cl:
        temp = []
        i, j = row, col

        while i < rl and j >= 0:
            temp.append(matrix[i][j])
            i += 1
            j -= 1

        if (row + col) % 2 == 0:
            res.extend(temp[::-1])
        else:
            res.extend(temp)

        if col < cl -1:
            col += 1
        else:
            row += 1

    return res


print(findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# >>> [1,2,4,7,5,3,6,8,9]


# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 196 ms
# Memory Usage: 16.1 MB
