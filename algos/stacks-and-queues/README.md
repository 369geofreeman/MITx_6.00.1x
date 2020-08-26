# Stacks and Queues

##  Big O:

### Using deque

A deque (double-ended queue) is represented internally as a doubly linked list. 
(Well, a list of arrays rather than objects, for greater efficiency.) 
Both ends are accessible, but even looking at the middle is slow, 
and adding to or removing from the middle is slower still.

| Operation   | Average Case | Amortized Worst Case |
|-------------|--------------|----------------------|
|  Copy       | O(n)         | O(n)                 |
|  append     | O(1)         | O(1)                 |
|  appendleft | O(1)         | O(1)                 |
|  pop        | O(1)         | O(1)                 |
|  popleft    | O(1)         | O(1)                 |
|  extend     | O(k)         | O(k)                 |
|  extendleft | O(k)         | O(k)                 |
|  rotate     | O(k)         | O(k)                 |
|  remove     | O(n)         | O(n)                 |
