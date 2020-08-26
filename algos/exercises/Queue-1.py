# Queue
# Exercise-1



 #Design a food ordering system where your python program will run two threads,
 #
 #Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
 #Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
 #Use this video to get yourself familiar with multithreading in python
 #
 #Pass following list as an argument to place order thread,
 #
 #orders = ['pizza','samosa','pasta','biryani','burger']
 #This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.


from collections import deque
import time
import threading

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

q = Queue()

def place_order(orders):
    for food in orders:
        print('Order Placed: {}'.format(food))
        q.enqueue(food)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while q.is_empty() == False:
        food = q.dequeue()
        print('Order Served: {}'.format(food))
        time.sleep(2)


orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
t2.start()

t1.join()
t2.join()

















