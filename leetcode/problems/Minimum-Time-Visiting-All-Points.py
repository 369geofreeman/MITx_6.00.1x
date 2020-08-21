# Minimum Time Visiting All Points

# On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.
# 
# You can move according to the next rules:
# 
# In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.
#  
# 
# Example 1:
# 
# 
# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds
# Example 2:
# 
# Input: points = [[3,2],[-2,2]]
# Output: 5
#  
# 
# Constraints:
# 
# points.length == n
# 1 <= n <= 100
# points[i].length == 2
# -1000 <= points[i][0], points[i][1] <= 1000

def minTimeToVisitAllPoints(points):
    pointA = points[0][0]
    pointB = points[0][1]
    count = 0

    for i in points[1:]:
        while pointA != i[0] or pointB != i[1]:
            if pointA<i[0]: pointA+=1
            if pointA>i[0]: pointA-=1
            if pointB<i[1]: pointB+=1
            if pointB>i[1]: pointB-=1
            count+=1
    return count



print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
# >>> 7
print(minTimeToVisitAllPoints([[3,2],[-2,2]]))
# >>> 5



# 122 / 122 test cases passed.
# Status: Accepted
# Runtime: 2632 ms
# Memory Usage: 13.9 MB
