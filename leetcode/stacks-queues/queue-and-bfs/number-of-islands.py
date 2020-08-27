# Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# 
# 
# 
# Example 1:
# 
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
# 
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


def numIslands(grid):
    # if no grid return 0
    if not grid:
        return 0

    # Set count to 0
    count = 0

    # Search through each node looking for a "1"
    # if found use DFS to mark that 'island' as found
    # Increment count by 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
        # print(grid) uncheck this to watch it in action (each row is a result)
    return count

def dfs(grid, i, j):
    # Starting from the source (node we found a "1" on)
    # Mark each "1" as a "#" so we don't vist the same one twice
    # If no "1" then return as 'island' will be all "#"'s
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)



grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid1))
# >>> 1
print(numIslands(grid2))
# >>> 3




# 47 / 47 test cases passed.
# Status: Accepted
# Runtime: 156 ms
# Memory Usage: 14.8 MB
