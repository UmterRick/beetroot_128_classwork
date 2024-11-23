"""
Queue - First In First Out (FIFO)
"""
from collections import deque



class Queue:
    def __init__(self):
        self.__items = []


    def push(self, new_item):
        self.__items.append(new_item)


    def pop(self):
        return self.__items.pop(0)

    def get(self):
        return self.__items[0]

    def __str__(self):
        return str(self.__items)

    def __ne__(self, other):
        return self.__items == other

    def __eq__(self, other):
        return self.__items == other

    def __len__(self):
        return len(self.__items)




d = deque()

stack = deque()

stack.append(1)
stack.pop()


queue = deque()

queue.append()
queue.popleft()



