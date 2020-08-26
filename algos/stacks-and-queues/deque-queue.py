# Queue example using deque

from collections import deque

q = deque()

q.appendleft('first')
q.appendleft('second')
q.appendleft('third')

print(q.pop())
print(q)
