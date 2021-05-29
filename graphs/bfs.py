#BFS - Busca em Largura

from typing import DefaultDict


class GraphBfs:
    
    def __init__(self):
        # Create list start cod
        self.graph = DefaultDict(list)

    #function add the node in graph
    def addEdge(self, index, vertex):
        self.graph[index].append(vertex)

    #function of print bfs | add primary node visited
    def BFS(self, node):
        #vertex not viseted add false
        visited = [False] * (len(self.graph))

        #created list empty of graph bfs
        listQueue = []

        #add node visited in stack
        listQueue.append(node)
        visited[node] = True

        while listQueue:
            node = listQueue.pop(0)
            print(node, " ")

            for i in self.graph[node]:
                if visited[i] == False:
                    listQueue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    
    g = GraphBfs() 
    g.addEdge(0, 2) 
    g.addEdge(0, 3) 
    g.addEdge(0, 4) 
    g.addEdge(1, 2) 
    g.addEdge(1, 4) 
    g.addEdge(2, 4)
    g.addEdge(3, 4) 
    g.addEdge(3, 5) 
    g.addEdge(4, 5) 
    g.addEdge(5, 1)  
    
    print ("Segue a execução do BFS, começando pelo vértice 2")
    g.BFS(0) 