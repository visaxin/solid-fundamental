class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def clear(self):
        del self.items[:]
    def empty(self):
        return self.size() == 0
    def top(self):
        return self.items[self.size()-1]
#application 10 to 2
def divby2(decNumber):

    s = Stack()

    while decNumber > 0:
        rem = decNumber % 2

        s.push(rem)
        decNumber = decNumber // 2


    binString = ""

    while not s.empty():
        binString = binString + str(s.pop())

    return binString


def f():
    a = 0
    b = 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b



def f():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
