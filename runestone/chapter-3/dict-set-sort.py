# Devise an experiment that compares the performance of the del operator on lists and dictonaries


# Below are two functions that will get the average of 10 calls each to deleting items at a random index from a random list, and a random dictonary respectively
# As can be seen when running the test, we get similar results proving that 'del' for list and 'del' for dictonary both run equally at O(n).



import time
from random import randrange

def delLst():
    times = 0
    for i in range(1000,10000,1000):
        listA = [randrange(1000) for x in range(i)]
        start = time.time()
        del listA[randrange(len(listA))]
        end = time.time()
        times += (end-start)
    return (times/10)


def delDict():
    times = 0
    for i in range(1000,10000,1000):
        lst = {randrange(1000) for x in range(i)}
        dictA = dict(enumerate(lst))
        start = time.time()
        del dictA[randrange(len(dictA))]
        end = time.time()
        times += (end-start)
    return (times/10)






print('The average run time for del on a dictonary is: ', delDict())
print('The average run time for del on a list is: ', delLst())


