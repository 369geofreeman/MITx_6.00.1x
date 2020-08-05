# The old switcheroo 2


# def encode(str)
# that takes in a string str and replaces all the letters with their respective positions in the English alphabet.
# 
# encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
# encode('codewars') == '315452311819'
# encode('abc-#@5') == '123-#@5'

import string
alph = string.ascii_lowercase

def encode(string):
    s = list(string)
    for i,v in enumerate(s):
        if v.lower() in alph:
            index = alph.index(v.lower())
            s[i] = str(index+1)
    return "".join(s)





print(encode('abc-#@5'))
# '123-#@5'
print(encode('ZzzzZ'))
# 2626266226
print(encode('this is a long string!! Please [encode] @C0RrEctly'))
# '208919 919 1 1215147 1920189147!! 161251195 [51431545] @30181853201225'
