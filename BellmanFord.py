from collections import defaultdict
import math
import sys

class Graph:
    def __init__(self, V):
        self.graph = []
        self.V = V

    def addEdge(self, u, v, w):
        self.graph.append((u, v, w))

    def BellmanFord(self, source):
        distance=[math.inf]*(self.V)
        parent = [None]*(self.V)

        distance[source]=0
        for i in range(self.V-1 ):
            for u, v, w in self.graph:
                if(distance[v] > distance[u]+w):
                    distance[v] = distance[u]+w
                    parent[v]=u

        for u, v, w in self.graph:
            if(distance[v]>distance[u]+w):
                print("Error h bhai!")
                sys.exit()

        print(distance)

g= Graph(5)
g.addEdge(0,1,-1)
g.addEdge(0,2,4)
g.addEdge(1,2,3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.BellmanFord(0)

