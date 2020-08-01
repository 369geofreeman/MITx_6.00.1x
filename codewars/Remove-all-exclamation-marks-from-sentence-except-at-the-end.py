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
    if s[-1] != '!': return s
    index = 0
    for i in range(len(s[::-1])):
        if s[::-1][i] != '!': index = i+1
    return s.replace('!', '') + ('!'*index)



print(remove('!Hi!!!!!!!'))
print(remove('Hi!!!'))
print(remove('!Hi'))
