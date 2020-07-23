# Problem 2

# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2


s = 'azcbobobegghakl'

bobcount = 0
for position in range(len(s)+1):
    if position+3 > len(s):
        break
    if s[position:position+3] == 'bob':
        bobcount += 1
print("Number of times bob occurs is: " + str(bobcount))
