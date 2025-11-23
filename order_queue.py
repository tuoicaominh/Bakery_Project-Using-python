# order_queue.py

from collections import deque

class OrderQueue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, order):
        self.q.append(order)

    def dequeue(self):
        return self.q.popleft() if self.q else None

    def list_all(self):
        return list(self.q)