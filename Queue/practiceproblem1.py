import time
from collections import deque
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

foodOrderQueue = Queue()

def placeOrders (orderlist) :
    for order in orders:
        print(f"Placing  the order for: {order}")
        foodOrderQueue.enqueue(order)
        time.sleep(0.5)
        

def serveOrder () :
    for order in orders:
        order = foodOrderQueue.dequeue()
        print(f"Here is your order: {order}")
        time.sleep(2)
        

if __name__ == '__main__' :
    orders = ['pizza','samosa','pasta','biryani','burger']

    orderPlaing = threading.Thread(target= placeOrders, args= (orders,))
    orderServing = threading.Thread(target= serveOrder)

initialTime = time.time()
orderPlaing.start()
time.sleep(1)
orderServing.start()

orderPlaing.join()
orderServing.join()

finalTime = time.time()

print(finalTime-initialTime)