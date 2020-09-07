# Linked Lists - Insert Nth
# 
# Implement an InsertNth() function (insert_nth() in PHP) which can insert a new node at any index within a list.
# 
# InsertNth() is a more general version of the Push() function that we implemented in the first kata listed below. Given a list, an index 'n' in the range 0..length, and a data element, add a new node to the list so that it has the given index. InsertNth() should return the head of the list.
# 
# insertNth(1 -> 2 -> 3 -> null, 0, 7) === 7 -> 1 -> 2 -> 3 -> null)
# insertNth(1 -> 2 -> 3 -> null, 1, 7) === 1 -> 7 -> 2 -> 3 -> null)
# insertNth(1 -> 2 -> 3 -> null, 3, 7) === 1 -> 2 -> 3 -> 7 -> null)
# You must throw/raise an exception (ArgumentOutOfRangeException in C#, InvalidArgumentException in PHP) if the index is too large.


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_nth(head, index, data):
    if head is None and index > 0: raise ValueError()
    if head is None or index == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    head.next = insert_nth(head.next, index-1, data)
    return head
