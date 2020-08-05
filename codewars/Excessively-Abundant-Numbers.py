# Excessively Abundant Numbers


# An abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself.
# 
# The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).
# 
# Derive function abundantNumber(num)/abundant_number(num) which returns true/True/.true. if num is abundant, false/False/.false. if not.

def abundant_number(num):
    count = 0
    for i in range(1,num):
        if num%i==0:
            count += i
    return count>num



print(abundant_number(18))
# True
print(abundant_number(37))
# False
print(abundant_number(120))
# True
