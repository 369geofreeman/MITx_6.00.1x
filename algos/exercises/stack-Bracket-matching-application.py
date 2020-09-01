# Bracket-matching application

# A function that will verify whether a statement containing brackets--(, [, or {--is balanced, that is, whether the number of closing brackets matches the number of opening brackets. It will also ensure that one pair of brackets really is contained in another:


# First set up our stack

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size +=1

    def pop(self):
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
        if self.top:
            return self.top.data
        else:
            return None


# Now define our bracket matching application

def check_bracket(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('(', '[', '{'):
            stack.push(ch)
        if ch in (')', ']', '}'):
            last = stack.pop()
        else: continue
        if last == '(' and ch == ')':
            continue
        elif last == '[' and ch == ']':
            continue
        elif last == '{' and ch == '}':
            continue
        else:
            return False

    if stack.size > 0:
        return False
    else:
        return True


# Check the code

s1 = ( "{(foo)(bar)}[hello](((this)is)a)test",
      "{(foo)(bar)}[hello](((this)is)atest",
      "{(foo)(bar)}[hello](((this)is)a)test))"
)

for s in s1:
    m = check_bracket(s)
    print("{}: {}".format(s,m))

# >>> {(foo)(bar)}[hello](((this)is)a)test: True
# >>> {(foo)(bar)}[hello](((this)is)atest: False
# >>> {(foo)(bar)}[hello](((this)is)a)test)): False






