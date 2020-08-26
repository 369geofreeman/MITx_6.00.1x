# Class version of a Stack using deque

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return  self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

reverseStack = Stack()

reverseStack.push(22)
reverseStack.push(369)
reverseStack.push('GeoFr33man')
reverseStack.push(333)
reverseStack.push('Hi, how are you?')

print(reverseStack.size())

