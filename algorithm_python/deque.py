#double =ended queue

#using list
class Deque():
    """docstring for Deque"""
    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.insert(0,item)

    def addRear(self,item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)
    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def empty(self):
        return self.size() == 0
#using collections.Deque

from collections import deque
class Deque():
    def __init__(self):
        self.items = deque()
    def addFront(self,item):
        self.items.appendleft(item)
    def addRear(self,item):
        self.items.append(item)
    def removeFront(self):
        return self.items.popleft()

    def removeRear(self):
        return self.items.pop()
    def empty(self):
        return self.size() == 0
    def size(self):
        return len(self.items)
#application
#exame palindrome  eg: abcba
#extract from front and rear at the same time
#compare them.
