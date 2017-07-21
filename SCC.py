from collections import defaultdict
count=0

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addNode(self, init, connect):
        self.graph[init].append(connect)

    def DFStrigger(self, index, visited, stack):
        visited[index] =True

        for ele in self.graph[index]:
            if(visited[ele]==False):
                self.DFStrigger(ele, visited, stack)
        stack.append(index)

    def DFS(self, stack):
        visited=[False]*(count)

        for i in range(count):
            if(visited[i]==False):
                self.DFStrigger(i, visited, stack)

    def DFSUtil(self, i, visited):
        visited[i]=True
        print(i, end=' ')
        for k in self.graph[i]:
            if(visited[k]==False):
                self.DFSUtil(k, visited)

    def PrintSCC(self, g, stack):
        visited=[False]*(count)
        for i in reversed(stack):
            if(visited[i]==False):
                g.DFSUtil(i, visited)
                print("")


    def triggerSCC(self, stack):
        g = Graph()
        for i in self.graph:
            for ele in self.graph[i]:
                g.addNode(ele, i)

        self.PrintSCC(g, stack)


    def SCC(self):
        stack = []
        self.DFS(stack)
        #print(stack)
        self.triggerSCC(stack)


gr = Graph()
count=4
gr.addNode(0, 1)
gr.addNode(1, 2)
gr.addNode(2, 0)
gr.addNode(3, 2)

gr.SCC()