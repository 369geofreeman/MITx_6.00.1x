# Split a String in Balanced Strings



# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# 
# Given a balanced string s split it in the maximum amount of balanced strings.
# 
# Return the maximum amount of splitted balanced strings.

#Example 1:
#
#Input: s = "RLRRLLRLRL"
#Output: 4
#Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
#Example 2:
#
#Input: s = "RLLLLRRRLR"
#Output: 3
#Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
#Example 3:
#
#Input: s = "LLLLRRRR"
#Output: 1
#Explanation: s can be split into "LLLLRRRR".
#Example 4:
#
#Input: s = "RLRRRLLRLL"
#Output: 2
#Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'



def balancedStringSplit(s):
    bal = 0
    count = 0
    for i in s:
        if i == "L":
            bal+=1
        else:
            bal-=1
        if bal == 0:
            count += 1
    return count


print(balancedStringSplit("RLRRLLRLRL"))
# >>> 4
print(balancedStringSplit("RLLLLRRRLR"))
# >>> 3
print(balancedStringSplit("RLRRRLLRLL"))
# >>> 2


# Runtime: 28 ms, faster than 83.05% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 13.9 MB, less than 25.07% of Python3 online submissions for Split a String in Balanced Strings

# 40 / 40 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.9 MB.
