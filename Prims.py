from collections import defaultdict
import heapq

class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v, w):
        self.graph[u].append((u, v, w))
        self.graph[v].append((v, u, w))

    def MSTPrim(self, root):
        key=[0]*(self.V)
        parent = [None]*(self.V)

        for vertex in self.graph:
            key[vertex] = 100000
            parent[vertex] = None

        key[root] = 0
        k=[]
        for i in range(self.V):
            heapq.heappush(k, (key[i],i))

        heapq.heapify(k)

        while(len(k)>0):
            u = heapq.heappop(k)
            for v in self.graph[u[1]]:
                try:
                    w = [i[1] for i in k if(i[1]==v[1])][0]
                except:
                    w='False'
                if(key[v[1]]>v[2] and w!='False'):
                    key[v[1]]=v[2]
                    parent[v[1]]=u[1]

        print(key)
        print(parent)

g = Graph(9)
g.addEdge(0,1,4)
g.addEdge(0,7,8)
g.addEdge(1,2,8)
g.addEdge(1,7,11)
g.addEdge(2,3,7)
g.addEdge(2,8,2)
g.addEdge(2,5,4)
g.addEdge(3,4,9)
g.addEdge(3,5,14)
g.addEdge(4,5,10)
g.addEdge(5,6,2)
g.addEdge(6,7,1)
g.addEdge(6,8,6)
g.addEdge(7,8,7)
g.MSTPrim(0)