# Problem 1

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

s = 'bverbvueueghfjeiojdfgaaeu§'

v = 'aeiou'
res = [l for l in s if l in v]
print(len(res))
