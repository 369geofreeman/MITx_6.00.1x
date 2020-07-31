# Simple Array product

# In this Kata, you will be given a multi-dimensional array containing 2 or more sub-arrays of integers. Your task is to find the maximum product that can be formed by taking any one element from each sub-array.
# 
# Examples:
# solve( [[1, 2],[3, 4]] ) = 8. The max product is given by 2 * 4
# solve( [[10,-15],[-1,-3]] ) = 45, given by (-15) * (-3)
# solve( [[1,-1],[2,3],[10,-100]] ) = 300, given by (-1) * 3 * (-100



def solve(arr):
    arrRes = []
    res = 1
    for i in arr:
        res *= max(i, key=lambda x: abs(x))
    return res


print(solve([[-11,-6],[-20,-20],[18,-4],[-20, 1]]))
# res 17600
