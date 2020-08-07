# Devise an experiment to verify that the list index operator is O(1)

# Results below will have a similar time if list index operator is O(1)


import time
from random import randrange


for i in range(1000, 10000, 1000):
    listA = [randrange(1000) for x in range(i)]
    start = time.time()
    res = listA[randrange(len(listA))]
    end = time.time()
    print("Found Index: {} in {}.".format(res, end-start))





import time
from random import randrange



