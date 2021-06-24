from typing import DefaultDict
import pandas as pd


class GraphBfs:
    def __init__(self):
        # Create list start cod
        self.graph = DefaultDict(list)

    #function add the node in graph
    def add_edge(self, index, vertex):
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
            print(f'visitando o vertice: {node}', ' ')

            for i in self.graph[node]:
                if visited[i] == False:
                    listQueue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    # Area de teste do algorimo

    # Entre com seu grafo no arquivo graphEnter.csv
    graph = pd.read_csv("assets/graphEnter.csv", sep=';', header=0, engine='python')
    lista = graph.values
    
    g = GraphBfs()
    
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] != 0:
                g.add_edge(i, j)

    g.BFS(int(input("Digite o vertice de saida: "))) 