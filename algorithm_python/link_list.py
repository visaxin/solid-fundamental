class Node():
    """docstring for Node"""
    def __init__(self, val):

        self._val = val
        self._next = None
    def getVal(self):
        return self._val
    def setVal(self,val):
        self._val = val
    def getNext(self):
        return self._next

        tmp = Node(item)
        tmp.setNext(self.head.getNext())
        self.head.setNext(tmp)

    def remove(self,item):
        prev = self.head
        while prev.getNext() != self.head:
            cur = prev.getNext()
            if cur.getVal() == item:
                prev.setNext(cur.getNext())
            cur = cur.getNext()

    def search(self,item):
        cur = self.head.getNext()
        while cur != self.head:
            print cur.getVal()
            if cur.getVal() == item:
                return True
            cur = cur.getNext()

    def empty(self):
        return self.head.getNext() == self.head
    def size(self):
        cur = self.head.getNext()
        count = 0
        while cur != self.head:
            count += 1
            cur = curl.getNext()
        return count


if __name__ == '__main__':
    s = Link_list()

    print s.empty()
    print s.size()
    s.add(2)
    s.add(3)
    print s.search(2)
