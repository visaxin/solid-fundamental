import sys

class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.adj = {}

    def addNeighbor(sefl,nbr,weight=0):
        self.adj[nbr] = weight



class Graph(object):
    def __init__(self):
        self.vertexlist = {}
        self.size = 0

    def addVertex(self,key):
        vertex = Vertext(key)
        self.vertextlist[key] = vertex
        self.size +=1
        return vertext

    def getVertex(self,key):
        return self.vertextlist.get(key)

    def addEdge(self,f,t,weight=0):
        if f not in self.vertexlist:
            self.addVertext(f)
        if t not in self.vertexlist:
            self.addVertext(t)
        self.vertexlist[f].addNeighbor(self.vertexlist[t],weight)

    def __iter__(self):
        return iter(self.vertexlist.values())
class PriorityQueue(object):
    def __init__(self,path):
        self.path= path
        self.queue = []
        self.size = 0
    def buildHeap(self,alist):
        self.queue = alist
        self.size = len(alist)
        for i in xrange(self.size/2-1,0,-1):
            self._perDown(i)
    def _perDown(self,i):
        left = 2*i + 1
        righ = 2*i +2
        little = i
        
def Dijkstra(G,s):
    path = {}
    vertexlist = []

    for v in G:
        vertexlist.append(v)
        path[v] = sys.maxsize

    path[s] = 0
    queue = PriorityQueue(path)


if __name__ == '__main__':
    g = Graph()
    g.addEdge('u','x',1)

    u = g.getVertex('u')
    path = Dijkstra(g,u)
