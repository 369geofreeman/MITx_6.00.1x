# Given a list of numbers in random order, write an algorithm that works in 𝑂(𝑛log(𝑛)) to find the kth smallest number in the list.

# Running pythons built in sort method with achieve a O(n) result, so using a for loop we can access the Kth element and bring the algorithm to O(n log(n))



def getK(lst, index):
    # Gets the Kth smallest element from a list

    lst.sort()

    for i in range(len(lst)):
        if i == index:
            return lst[i-1]



aList = [11,23,4,5,123,643,7,9,34]


print('O(n log(n)) result: ', getK(aList,2))




# Improved the algorithm to be linear O(n)
# Only one loop is relevant and Pythons built in method sort does the trick. Then we can use simple O(1) list indexing to find the value of index K.



def getLinearK(lst,index):
    lst.sort()
    return lst[index-1]


print('Linear O(n) result: ', getLinearK(aList, 2))
