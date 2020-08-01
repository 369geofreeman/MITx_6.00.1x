# Return-Two-Highest-Values-in-List:


# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.
# 
# The result should also be ordered from highest to lowest.
# 
# Examples:
# 
# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []



def two_highest(arg1):
    if arg1 == []: return []
    if len(arg1) == 1: return arg1
    lst = sorted(set(arg1))
    return [lst[-1],lst[-2]]



print(two_highest([15, 20, 20, 17]))
# [20, 17]
