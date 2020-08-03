# SevenAte9

# Write a function that removes every lone 9 that is inbetween 7s.

# seven_ate9('79712312') => '7712312'
# seven_ate9('79797') => '777'
# Input: String Output: String


def seven_ate9(str_):
    res = list(str_)
    for i in range(len(str_)):
        if str_[i:i+3] == '797':
            res[i+1] = ''
    return "".join(res)



print(seven_ate9('165561786121789797'))
# '16556178612178977')
print(seven_ate9('7979797'))
# ,'7777')
