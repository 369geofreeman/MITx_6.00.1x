# Devise an experiment to verify that get item and set item are O(1) for dictonaries 


# Below are two functions that will get the average of 10 calls to set and get items respectivley
# As the results show they are both running in O(1) time

import time
from random import randrange

def getItem():
    times = 0
    for i in range(1000,10000,1000):
        listA = [randrange(1000) for x in range(i)]
        start = time.time()
        listA[randrange(len(listA))]
        end = time.time()
        times += (end-start)
    return (times/10)


def setItem():
    times = 0
    for i in range(1000,10000,1000):
        lst = {randrange(1000) for x in range(i)}
        dictA = dict(enumerate(lst))
        start = time.time()
        dictA[randrange(len(dictA))] = 'newItem'
        end = time.time()
        times += (end-start)
    return (times/10)






print('The average run time for setting an item in a dictonary is: ', setItem())
print('The average run time for getting an item fromn a dictonaryt is: ', getItem())

