import queue
class Graph:
    def __init__(self, nvertices):
        self.nVertices = nvertices
        self.adjMatrix = [[0 for i in range(nvertices)]for j in range(nvertices)]

    def addEdge(self, v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __bfs(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            u = q.get()
            print(u, end = " ")
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
        
    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfs(i, visited)
        print()

    def __dfsHelper(self, sv, visited):
        
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if (self.adjMatrix[sv][i] > 0 and visited[i] is False):
                self.__dfsHelper(i, visited)
    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(0,visited)
    
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def containsEdge(self,v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def __str__(self):
        return str(self.adjMatrix)


V,E = map(int, input().split(' '))
g = Graph(V)
for i in range(E):
    v1, v2 = map(int, input().split(' '))
    g.addEdge(v1, v2)

g.bfs()