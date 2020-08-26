# Multi Threading

# A way to run multible threads (functions) at once. in this basic example we are running two functions to calculate the squares and cubes of a set of numbers respectively.

# Read more from the docs here: https://docs.python.org/3/library/threading.html


# First import the library. I'll also use time to time the functions
import time
import threading


# Function to get squares of the numbers in a list
def squares(val):
    for i in val:
        time.sleep(0.4)
        print('Square: ', i*i)

# Function to get the cubes of the numbers in a list
def cubes(val):
    for i in val:
        time.sleep(0.4)
        print('Cube: ', i*i*i)


# The arguments (a list of nums)
nums = [2,3,4,5,6]


# variable to store the time before execution
t = time.time()

# Store the functions in variable wrapped in the Thread call from the  threading library
t1 = threading.Thread(target=squares, args=(nums,))
t2 = threading.Thread(target=cubes, args=(nums,))

# initiate the functions
t1.start()
t2.start()

# output the results as they come in from the functions
t1.join()
t2.join()

# Out put the results of the time it took to run
print('Done in {} seconds'.format(time.time()-t))
