from collections import defaultdict

import math


class Graph:
    def __init__(self, V):
        self.graph = []
        self.V = V
        self.rank = [0]*(self.V)
        self.parent = [None]*(self.V)

    def addEdge(self, u, v, w):
        self.graph.append([w,v,u])

    def makeset(self, u):
        self.rank[u]=0
        self.parent[u]=u

    def findset(self, u):
        if(self.parent[u]!=u):
            u = self.findset(self.parent[u])
        return self.parent[u]

    def Union(self, u , v):
        rank1 = self.rank[self.findset(u)]
        rank2 = self.rank[self.findset(v)]

        if(rank1>rank2):
            self.parent[self.findset(v)] = self.findset(u)
        else:
            self.parent[self.findset(u)] = self.findset(v)
            if(rank1==rank2):
                self.rank[self.findset(v)]+=1

    def Kruskal(self):
        for vertex in range(self.V):
            self.makeset(vertex)

        edges = self.graph
        edges.sort()

        MST=[]

        for edge in edges:
            if(self.findset(edge[1])!=self.findset(edge[2])):
                MST.append(edge)
                self.Union(edge[1], edge[2])

        weight=0
        for ele in MST:
            weight+=ele[0]
        #print(weight, MST)
        return (weight, MST)

    def secondMST(self, MST):
        init_graph = self.graph[:]
        MSTs=[]
        for vertex in MST:
            for element in self.graph:
                if(vertex is element):
                    save = element[0]
                    element[0]=math.inf
                    x, y = self.Kruskal()
                    MSTs.append((x,y))
                    element[0]=save
                    self.graph = init_graph[:]
                    break

        MSTs.sort()
        print(MSTs[1])



g=Graph(9)
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
(weight, MST) = g.Kruskal()
#print(weight, MST)
g.secondMST(MST)

