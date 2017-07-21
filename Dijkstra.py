from collections import defaultdict
import math
import heapq

class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v, w):
        self.graph[u].append((u, v, w))

    def Dijkstra(self, source):
        distance = [math.inf]*(self.V)
        parent = [None]*(self.V)

        distance[source]=0
        queue = []
        Visited=[]
        #print(self.graph)

        # for k in range(self.V):
        #     l = self.graph[k]
        #     for temp in l:
        #         heapq.heappush(queue, (distance[temp[0]], temp[1], temp[0]))

        heapq.heappush(queue, (0, source))

        while(len(queue)>0):
            w, u = heapq.heappop(queue)
            #print(queue)
            Visited.append(u)
            for l, m, n in self.graph[u]:
                if(distance[m]>distance[l]+n):
                    distance[m]=distance[l]+n
                    print(m, distance[m])
                    parent[m]=l
                    heapq.heappush(queue, (distance[m], m))
        print(distance)
        print(Visited)

g = Graph(5)
g.addEdge(0,1,10)
g.addEdge(1,2,1)
g.addEdge(2,3,4)
g.addEdge(3,2,6)
g.addEdge(3,0,7)
g.addEdge(4,3,2)
g.addEdge(4,2,9)
g.addEdge(4,1,3)
g.addEdge(1,4,2)
g.addEdge(0,4,5)
g.Dijkstra(0)