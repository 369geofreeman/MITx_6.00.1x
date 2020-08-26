# Exercise Queue 2


# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.
# 
# You also need to add front() function in queue class that can return the front element in the queue.

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)



def tenBinNums():
    # Using a queue
    # Prints the first 10 numbers in binary format
    q = Queue()
    for i in range(1,11):
        binNum = bin(i)[2:]
        q.enqueue(binNum)

    while not q.is_empty():
        num = q.dequeue()
        print(num)


tenBinNums()
