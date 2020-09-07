# Linked Lists - Get Nth
# 
# Implement a GetNth() function that takes a linked list and an integer index and returns the node stored at the Nth index position. GetNth() uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on. So for the list 42 -> 13 -> 666, GetNth() with index 1 should return Node(13);
# 
# getNth(1 -> 2 -> 3 -> null, 0).data === 1
# getNth(1 -> 2 -> 3 -> null, 1).data === 2
# The index should be in the range [0..length-1]. If it is not, GetNth() should throw/raise an exception (ArgumentException in C#, InvalidArgumentException in PHP). You should also raise an exception (ArgumentException in C#, InvalidArgumentException in PHP) if the list is empty/null/None.
# 
# Prerequisite Kata (may be in beta):
# 
# Linked Lists - Push & BuildOneTwoThree
# Linked Lists - Length & Count
# The push() and buildOneTwoThree() (BuildOneTwoThree in C#, build_one_two_three() in PHP) functions do not need to be redefined.






class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def get_nth(node, index):
    # Your code goes here.
    if node is None or index <0: raise Exception()
    c = 0
    while node:
        if c == index:
            return node
        c+=1
        node = node.next
    raise Exception()
