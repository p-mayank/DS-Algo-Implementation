from collections import defaultdict
import sys

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph=defaultdict(list)
        self.indegree = [0]*(self.V)
        self.outdegree = [0]*(self.V)

    def Check(self):
        for ele in range(self.V):
            if(self.indegree[ele]!=self.outdegree[ele]):
                print("No euler path found.")
                sys.exit()


    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v]+=1
        self.outdegree[u]+=1

    def DFSUtil(self, Visited, Stack, i):
        Visited[i]=True

        for k in self.graph[i]:
            if(Visited[k]==False):
                self.DFSUtil(Visited, Stack, k)

        Stack.insert(0, i)

    def DFS(self):
        Visited=[False]*(self.V)
        Stack=[]

        for i in range(self.V):
            if(Visited[i]==False):
                self.DFSUtil(Visited, Stack, i)

        self.Transpose(Stack)

    def Transpose(self, Stack):
        g = Graph(self.V)
        for u in range(self.V):
            for v in self.graph[u]:
                g.addEdge(v, u)

        self.SCC(g, Stack)

    def FindSCC(self, ele, Visited):
        Visited[ele]=True
        #print(ele, end=" ")

        for i in self.graph[ele]:
            if(Visited[i]==False):
                self.FindSCC(i, Visited)


    def SCC(self, g, Stack):
        Visited=[False]*(self.V)
        count=0
        for ele in Stack:
            if(Visited[ele]==False):
                count+=1
                if(count<=1):
                    g.FindSCC(ele, Visited)
                else:
                    print("No Euler Path")
                    sys.exit()
        print("Yes")


g=Graph(5)
g.addEdge(1,0)
g.addEdge(0,2)
g.addEdge(2,1)
g.addEdge(0,3)
g.addEdge(3,4)
g.addEdge(4,0)
g.Check()
g.DFS()