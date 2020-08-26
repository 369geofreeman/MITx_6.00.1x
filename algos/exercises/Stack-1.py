# Data structure tutorial exercise: Stack

# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"



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


def reverseStr(s):
    if not s: return None
    stack = Stack()
    res = ''

    [stack.push(i) for i in s]

    for i in range(stack.size()):
        res += stack.pop()
    return res



string = 'We will conquere covid-19'

print(reverseStr(string))
# >>> "91-DIVOC ereuqnoc lliw eW"
print(reverseStr('Zero to one'))
# >>> eno ot oreZ
