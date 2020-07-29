# String Formating


# Given an integer, n, print the following values for each integer i  from 1 to x:
# 
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# The four values must be printed on a single line in the order specified above for each i from 1 to x. Each value should be space-padded to match the width of the binary value of n.




def print_formatted(number):
    l = len(bin(number))-1

    for x in range(1, number+1):
        print("{0:{r}d}{0:{e}o}{0:{e}X}{0:{e}b}".format(x, r=l-1, e=l))


print(print_formatted(17))
