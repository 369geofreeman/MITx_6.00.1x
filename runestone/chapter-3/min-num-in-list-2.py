# Minimum Number in list 2

# Find mionimum number is list using a linear method.

# An example of O(n)


import time
from random import randrange


def minNum(a):
    res = a[0]
    for i in a:
        if i< res:
            res = i
    return res


a = [2,4,7,3465,356,77,1,12,24]

print(minNum(a))



for listSize in range(1000,10001,1000):
    alist = [randrange(10000) for x in range(listSize)]
    start = time.time()
    print(minNum(alist))
    end = time.time()
    print("Size: {}. Time: {} ".format(len(alist), end-start))

