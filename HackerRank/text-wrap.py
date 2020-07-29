# coding=utf-8

# Text wrap

# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .


# You are given a string s and width w.
# Your task is to wrap the string into a paragraph of width w




def wrap(s, w):
    res = []
    for i in range(len(s)):
        if i % w == 0 and i > 0:
            res.append("\n")
        res.append(s[i])
    return "".join(res)


print(wrap(s,w))
