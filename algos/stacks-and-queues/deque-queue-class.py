# A Queue class using deque

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


pq = Queue()

pq.enqueue({
    'company': 'Wall Mrt',
    'timeStamp': '15 Apr, 11:01 AM',
    'price': 131.10
})

pq.enqueue({
    'company': 'Wall Mrt',
    'timeStamp': '15 Apr, 11:02 AM',
    'price': 132
})

pq.enqueue({
    'company': 'Wall Mrt',
    'timeStamp': '15 Apr, 11:03 AM',
    'price': 135
})

print(pq.buffer)
# >>> deque([{'company': 'Wall Mrt', 'timeStamp': '15 Apr, 11:03 AM', 'price': 135}, {'company': 'Wall Mrt', 'timeStamp': '15 Apr, 11:02 AM', 'price': 132}, {'company': 'Wall Mrt', 'timeStamp': '15 Apr, 11:01 AM', 'price': 131.1}])

print(pq.dequeue())
# >>> {'company': 'Wall Mrt', 'timeStamp': '15 Apr, 11:01 AM', 'price': 131.1}

print(pq.size())
# >>> 2
