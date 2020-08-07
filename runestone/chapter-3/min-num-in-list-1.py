# Minimum Number in list 1

# Compare each number to every other number on the list.

# An example of O(n²)

import time
from random import randrange

def minNum(a):
    res = a[0]
    for i in a:
        for x in a:
            if x < i and x < res:
                res = x
    return res



a = [2,4,7,3465,356,7,1,7,12,24]

print(minNum(a))


for listSize in range(1000,10001,1000):
    alist = [randrange(10000) for x in range(listSize)]
    start = time.time()
    print(minNum(alist))
    end = time.time()
    print("Size: {}. Time: {} ".format(len(alist), end-start))
