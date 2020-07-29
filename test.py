# import math
# import numpy as np
# import os
import string

# print(int(((2+4*6) % 4)*1+6//7+912*3*22*math.sqrt(4) +
#           int(np.array([3])+os.system("echo 2 > /dev/null"))))


s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w = 4


def wrap(s, w):
    res = []
    for i in range(len(s)):
        if i % w == 0 and i > 0:
            res.append("\n")
        res.append(s[i])
    return "".join(res)


print(wrap(s, w))
