
def Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self,item):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    def empty(self):
        return self.size() == 0
#application Josephus Problem

def josephus(namelist,num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for x in xrange(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()
