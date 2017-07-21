from collections import defaultdict
time=0
count=0

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addNode(self, init, connect):
        self.graph[init].append(connect)

    def TriggerDFS(self, source, visited):
        global time
        time+=1
        visited[source]=True
        print(source)
        for i in self.graph[source]:
            if(visited[i]==False):
                self.TriggerDFS(i, visited)
        time+=1

    def DFS(self, source):
        visited = [False]*(count)

        for i in range(count):
            if(visited[i]==False):
                self.TriggerDFS(i, visited)


if __name__ == '__main__':
    newG = Graph()
    print("Enter the connected nodes seperated by a space ")
    print("Type dfs <source_node> to print the DFS.")
    count =0
    k=input("> ")
    while (k.count('dfs')==0):
        count+=1
        init, connect = map(int, k.split())
        newG.addNode(init, connect)
        k=input("> ")

    k=k.split()
    source = int(k[1])
    newG.DFS(source)