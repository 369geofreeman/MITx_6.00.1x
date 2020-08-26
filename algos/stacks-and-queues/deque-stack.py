# An example of a stack using deque

from collections import deque

stack = deque()

stack.append(1)
stack.append(33)
stack.append('YOYOYO')
stack.append([1,2,3])

print(stack)

# remove from end LIFO (last in first out).

stack.pop()
# >>> Return s the last element of the stack, in this case [1,2,3]

print(stack)


# A simple stack written into a class

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek8(self):
        return  self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)



# Big O:
# A deque (double-ended queue) is represented internally as a doubly linked list. 
# (Well, a list of arrays rather than objects, for greater efficiency.) 
# Both ends are accessible, but even looking at the middle is slow, 
# and adding to or removing from the middle is slower still.

# | Operation   | Average Case | Amortized Worst Case |
# |-------------|--------------|----------------------|
# |  Copy       | O(n)         | O(n)                 |
# |  append     | O(1)         | O(1)                 |
# |  appendleft | O(1)         | O(1)                 |
# |  pop        | O(1)         | O(1)                 |
# |  popleft    | O(1)         | O(1)                 |
# |  extend     | O(k)         | O(k)                 |
# |  extendleft | O(k)         | O(k)                 |
# |  rotate     | O(k)         | O(k)                 |
# |  remove     | O(n)         | O(n)                 |
