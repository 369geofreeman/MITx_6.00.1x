# Problem 3

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc


s = 'azcbobobegghakl'
a = 'abcdefghijklmnopqrstuvwxyz'
tries = []
res = ''

for x in range(len(s)):
    for p in range(x, len(s)):
        if a.find(s[p]) < a.find(s[p-1]):
            break
        if p == x:
            res += s[p-1]
        res += s[p]
    tries.append(res)
    res = ''
print("Longest substring in alphabetical order is: {}".format(max(tries, key=len)))
