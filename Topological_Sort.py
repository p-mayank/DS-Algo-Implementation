from collections import defaultdict

class Graph:
    def __init__(self, count):
        self.length = count
        self.graph = defaultdict(list)

    def addNode(self, init, connect):
        self.graph[init].append(connect)

    def Topo_Sort(self, index, visited, stack):
        visited[index]=True

        for ele in self.graph[index]:
            if(visited[ele]==False):
                self.Topo_Sort(ele, visited, stack)

        stack.insert(0, index)


    def Topological(self):
        print(self.graph)
        visited = [False]*(self.length)
        stack=[]

        for i in range(self.length):
            if(visited[i]==False):
                self.Topo_Sort(i, visited, stack)

        print(stack)


if __name__ == '__main__':
    count=input("Type in the number of nodes:")
    newG = Graph(int(count))
    print("Enter the connected nodes seperated by a space ")
    print("Type tps to print the DFS.")
    k=input("> ")
    while (k.count('tps')==0):
        init, connect = map(int, k.split())
        newG.addNode(init, connect)
        k=input("> ")

    newG.Topological()