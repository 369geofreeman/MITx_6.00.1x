 # Letterbox Paint-Squad


# Story
# You and a group of friends are earning some extra money in the school holidays by re-painting the numbers on people's letterboxes for a small fee.
# 
# Since there are 10 of you in the group each person just concentrates on painting one digit! For example, somebody will paint only the 1's, somebody else will paint only the 2's and so on...
# 
# But at the end of the day you realise not everybody did the same amount of work.
# 
# To avoid any fights you need to distribute the money fairly. That's where this Kata comes in.
# 
# Kata Task
# Given the start and end letterbox numbers, write a method to return the frequency of all 10 digits painted.
# 
# Example
# For start = 125, and end = 132
# 
# The letterboxes are
# 
# 125 = 1, 2, 5
# 126 = 1, 2, 6
# 127 = 1, 2, 7
# 128 = 1, 2, 8
# 129 = 1, 2, 9
# 130 = 1, 3, 0
# 131 = 1, 3, 1
# 132 = 1, 3, 2
# The digit frequencies are 1 x 0, 9 x 1, 6 x 2 etc...
# 
# and so the method would return [1,9,6,3,0,1,1,1,1,1]
# 
# Notes
# 0 < start <= end
# In C, the returned value will be free'd.



def paint_letterboxes(start, finish):
    dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for x in range(start, finish+1):
        for i in list(map(int, str(x))): dict[i]+= 1
    return list(dict.values())



print(paint_letterboxes(125, 132))
# [1,9,6,3,0,1,1,1,1,1]
