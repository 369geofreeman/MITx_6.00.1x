# Filter unused digits

# Given few numbers, you need to print out the digits that are not being used.
# 
# Example:
# 
# unused_digits(12, 34, 56, 78) # "09"
# unused_digits(2015, 8, 26) # "3479"
# Note:
# 
# Result string should be sorted
# The test case won't pass Integer with leading zero



def unused_digits(*args):
    return "".join(number for number in "0123456789" if number not in str(args))



print(unused_digits(643))
#  "0125789")
print(unused_digits(864, 896, 744))
# "01235")
