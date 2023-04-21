import queue
from select import select
from sys import stdin
import sys
from tkinter import W
class Graph:
    def __init__(self, nvertices):
        self.nVertices = nvertices
        self.adjMatrix = [[0 for i in range(nvertices)]for j in range(nvertices)]

    def addEdge(self, v1,v2, wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt

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
    
    def dfsForConnectedOrNot(self, sv, visited):
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] == 1 and not visited[i] :
                self.dfsForConnectedOrNot(i, visited)
                visited[i] = True
    
    def isConnected(self):
        visited = [False for i in range(self.nVertices)]
        self.dfsForConnectedOrNot(0, visited)
        for boolVal in visited:
            if not boolVal:
                return False
        return True
    
    def dfsAllConnectedCompenents(self, vertex, visited, smallOutput):
        visited[vertex] = True
        smallOutput.append(vertex)

        for i in range(self.nVertices):
            if self.adjMatrix[vertex][i] == 1 and not visited[i]:
                self.dfsAllConnectedCompenents(i,visited,smallOutput)

    def allConnectedCompenents(self):
        visited = [False for i in range(self.nVertices)]
        finalList = []
        for i in range(len(visited)):
            if not visited[i]:
                smallOutput = list()
                cc = self.dfsAllConnectedCompenents(i, visited, smallOutput)
                finalList.append(smallOutput)
        return finalList
    
    def __hasPath(self, sv, ev, visited):
        if sv == ev:
            return True
        
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            u = q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] == 1 and not visited[i]:
                    if i == ev:
                        return True
                    q.put(i)
                    visited[i] = True
        return False

    def hasPath(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPath(sv, ev, visited)
    
    def __getMinVertex(self, visited , weight):
        min_vertex = -1
        for i in range(self.nVertices):
            if (visited[i] is False and (min_vertex == -1 or weight[min_vertex] > weight [i])):
                min_vertex = i
        return min_vertex


    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent = [ -1 for i in range(self.nVertices)]
        weight = [ sys.maxsize for i in range(self.nVertices)]
        weight[0] = 0
        for i in range(self.nVertices-1):
            min_vertex = self.__getMinVertex(visited, weight)
            visited[min_vertex] = True
        
            #Explore the neighbours of minVertex which is not visited
            #and update the weight corresponding to them if required
            for j in range(self.nVertices):
                if self.adjMatrix[min_vertex][j] > 0 and visited[j] is False:
                    if (weight[j] > self.adjMatrix[min_vertex][j]):
                        weight[j] = self.adjMatrix[min_vertex][j]
                        parent[j] = min_vertex
                
        for i in range(1, self.nVertices):
            if i < parent[i]:
                print(str(i) + " "+str(parent[i])+ " " + str(weight[i]))
            else:
                print(str(parent[i]) + " "+str(i)+ " " + str(weight[i]))

        
    def containsEdge(self,v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def __str__(self):
        return str(self.adjMatrix)




li = stdin.readline().strip().split()
V = int(li[0])
E = int(li[1])

g = Graph(V)
for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0], curr_input[1], curr_input[2])

print("prim's Algorithms")
g.prims()