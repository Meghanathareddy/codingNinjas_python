from logging.config import valid_ident
import queue
from select import select
from sys import stdin
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
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i,visited)
    
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __getPathDFS(self, sv, ev, visited):
        if sv == ev:
            return list([sv])
        
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] == 1 and not visited[i]:
                li = self.__getPathDFS(i, ev, visited)

                if li != None:
                    li.append(sv)
                    return li
        return None

    def getPathDFS(self, sv,ev):
        visited = [False for i in range(self.nVertices)]
        return self.__getPathDFS(sv,ev,visited)
    
    def __getPathBFS(self, sv, ev, visited):
        mapp = {}
        q = queue.Queue()
        if self.adjMatrix[sv][ev] == 1 and sv == ev:
            ans = []
            ans.append(sv)
            return ans
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            front = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[front][i] == 1 and visited[i] is False:
                    mapp[i] = front 
                    q.put(i)

                    visited[i] = True

                    if i == ev:
                        ans = []
                        ans.append(ev)
                        value = mapp[ev]
                        while value != sv:
                            ans.append(value)
                            value = mapp[value]
                        ans .append(value)
                        return ans
        return []

    
    def getPathBFS(self, sv, ev):

        #Return empty list in case of sv and ev is invalid
        if (sv > (self.nVertices - 1) or (ev > (self.nVertices - 1))):
            return list()
        
        visited = [False for i in range(self.nVertices)]
        return self.__getPathBFS(sv, ev, visited)
    
    def containsEdge(self,v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def __str__(self):
        return str(self.adjMatrix)


# V,E = map(int, input().split(' '))
# sv, ev = map(int, input().split(' '))
# g = Graph(V)
# for i in range(E):
#     v1, v2 = map(int, input().split(' '))
#     g.addEdge(v1, v2)

# print("dfs")
# g.dfs()
# print("bfs")
# g.bfs()
li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)

for i in range(E):
    arr = stdin.readline().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addEdge(fv, sv)

li = stdin.readline().strip().split()
sv = int(li[0])
ev = int(li[1])

li = g.getPathBFS(sv,ev)

if li != None:
    for element in li:
        print(element, end = " ")