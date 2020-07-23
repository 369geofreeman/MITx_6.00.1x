# Problem 1

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

s = 'bverbvueueghfjeiojdfgaaeu§'

count = 0
for num_vowels in s:
    if num_vowels == 'a' or num_vowels == 'e' or num_vowels == 'i' or num_vowels == 'o' or num_vowels == 'u':
        count += 1

print('Number of vowels:', count)
