# Remove-all-exclamation-marks-from-sentence-except-at-the-end


# Description:
# Remove all exclamation marks from sentence except at the end.
# 
# Examples
# remove("Hi!") == "Hi!"
# remove("Hi!!!") == "Hi!!!"
# remove("!Hi") == "Hi"
# remove("!Hi!") == "Hi!"
# remove("Hi! Hi!") == "Hi Hi!"
# remove("Hi") == "Hi"


def remove(s):
    ex = ''
    for i in s[::-1]:
        if i == '!':
            ex += i
        else:
            break
    res = s.replace('!', '')
    return res + ex


print(remove('!Hi!!!!!!!'))
print(remove('Hi!!!'))
print(remove('!Hi'))
