# 232. Implement Queue using Stacks
from collections import deque


class MyQueue(object):

    def __init__(self):
        self.queue = deque()

    def empty(self):
        return len(self.queue) == 0

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if not self.empty():
            return self.queue.popleft()

    def peek(self):
        if not self.empty():
            return self.queue[0]


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
