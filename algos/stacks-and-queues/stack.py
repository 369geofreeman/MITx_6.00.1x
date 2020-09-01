# Stack

# LIFO (last in first out)

# The functions associated with stack are: 
# - empty() – Returns whether the stack is empty – Time Complexity : O(1)
# - size() – Returns the size of the stack – Time Complexity : O(1)
# - peek() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
# - push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
# - pop() – Deletes the top most element of the stack – Time Complexity : O(1)


class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        # adds elemet to top of the list
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        # removes the top element and returns it
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        # Shows us the top element of the stack
        if self.top:
            return self.top.data
        else:
            return None

    def empty(self):
        # Tells us if the stack is empty
        if self.top == None:
            return True
        else:
            return False

    def size(self):
        # Return the size of the stack
        return self.size



myStack = Stack()

myStack.push(3)
myStack.push('Hi')
myStack.push(23)
myStack.push(47)
myStack.push('how are you?')

print('My stack size:', myStack.size)
print('top element:', myStack.peek())

myStack.pop()
myStack.pop()

print('removing 2 elements')
print('Is my stack empty?', myStack.empty())
print('Top element:', myStack.peek())
print('Stack size', myStack.size)


