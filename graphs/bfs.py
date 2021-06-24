from typing import DefaultDict
import pandas as pd


class GraphBfs:
    def __init__(self):
        self.graph = DefaultDict(list)


    def add_edge(self, index, vertex):
        self.graph[index].append(vertex)


    def BFS(self, node):
        visited = [False] * (len(self.graph))

        listQueue = []

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

    print('PS: lembre-se que nesse algoritmo pela implementação a matriz começa do 0')
    g.BFS(int(input("Digite o vertice de saida: "))) 