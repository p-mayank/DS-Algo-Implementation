heap=[]

def leftchild(i):
    return (2*i+1)

def rightchild(i):
    return (2*i+2)

def parent(i):
    return i//2

class heapq:
    def __init__(self):
        self.heap=[]
        self.length = 0

    def heappush(self, list, value):
        self.heap = list
        if(type(value) is list):
            for i in value:
                self.heap.append(i)
        else:
            self.heap(value)
        self.length+=1
        self.buildheap()

    def buildheap(self):
        for i in range((self.length-1)//2, -1, -1):
            self.minHeapify(i, self.length)

    def minHeapify(self, i, n):
        p = parent(i)
        l = leftchild(i)
        r = rightchild(i)

        if(l<n and self.heap[i]>self.heap[l]):
            smallest = l
        elif(r<n and self.heap[i]>self.heap[r]):
            smallest = r
        else:
            smallest = i

        if(smallest != i):
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest, n)

    def heappop(self, list):
        self.heap = list
        return self.heap[0]
        self.heap = self.heap[1:]
        self.length(len(list)-1)
