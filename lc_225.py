# 225. Implement Stack using Queues
from collections import deque


class MyStack(object):

    def __init__(self):
        self.stack = deque()
        self.length = 0

    def empty(self):
        return self.length == 0

    def push(self, x):
        self.stack.append(x)
        self.length += 1

    def pop(self):
        if not self.empty():
            popped_item = self.stack.pop()
            self.length -= 1
            return popped_item

    def top(self):
        if not self.empty():
            return self.stack[-1]


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
x = 20
param_4 = obj.empty()
print(param_4)
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
