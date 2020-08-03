# Binary Search

# DESCRIPTION:

# Example of Binary search using a list of the first 25 prime numbers where we find a prime by index.

# - For use with: sorted lists
# - How: Binary search works by reducing the list by half with every wrong guess. Every time we double the size of the array, we need at most one more guess
# - Speed: O(log(n))



# CODE:

def findPrimes(lst, target):
    min = 0
    max = len(lst)-1

    while min<=max:
        guess = (max+min)//2
        if lst[guess] == target: return target
        if lst[guess] < target:
            min = guess + 1
        else:
            max = guess -1
    return -1



# TESTS:


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

# 3 tests for a high prime, low prime and no prime.
res1 = findPrimes(primes, 73)
res2 = findPrimes(primes, 11)
res3 = findPrimes(primes, 10)

results = [res1,res2,res3]
for i in results:
    print('the index is {}'.format(i))

# the index is 73
# the index is 11
# the index is -1
