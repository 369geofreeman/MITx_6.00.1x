# List Comprehensions


# Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k s not equal to n.

x = 2
y = 2
z = 2
n = 2


print([[i, j, k] for i in range(x+1) for j in range(y+1)
       for k in range(z+1) if sum([i, j, k]) != n])
