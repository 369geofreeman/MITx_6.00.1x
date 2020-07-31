 # Stringy Strings


# write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
# 
# the string should start with a 1.
# 
# a string with size 6 should return :'101010'.
# 
# with size 4 should return : '1010'.
# 
# with size 12 should return : '101010101010'.
# 
# The size will always be positive and will only use whole numbers.



def stringy(s):
    return "".join([ '1' if x%2==0 else '0' for x in range(s) ])



print(stringy(12))
#, '101010101010'
