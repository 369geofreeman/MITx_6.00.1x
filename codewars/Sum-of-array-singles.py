# Sum of array singles
# ---



# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.
# 
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
# 
# More examples in the test cases.
# 
# Good luck!



def repeats(arr):
    res = []
    [res.append(i) for i in arr if arr.count(i) == 1]
    return res[0]+res[1]



print(repeats([16, 0, 11, 4, 8, 16, 0, 11]))
# 12
print(repeats([5, 17, 18, 11, 13, 18, 11, 13]))
# 22
