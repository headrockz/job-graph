import numpy as np
import pandas as pd


class InfoGraph:
    def __init__(self, graph):
        self.graph = graph
        #Mostrando o grafo
        self.printGraph()
        #Quantidade de Vertices
        self.numVertice()
        #Quantidade de arestas
        self.numArrest()
        #Grau de cada vertice
        self.numDegree()
        #Verifica se o grafo é euleriano ou unicursal
        self.graphEuleriano()

    # Imprime o grafo
    def printGraph(self):
        print(self.graph)
        print('')

    # Numero de arestas
    def numArrest(self):
        arrest = (self.graph.sum(axis=0).sum() / 2)
        print(f"Numero de arestas: {arrest}")

    # Numero de vertices
    def numVertice(self):
        vertice = len(self.graph)
        print(f"Numero de vertices: {vertice}")

    # Grau de cada vertice
    def numDegree(self):
        degree = self.graph.sum(axis=0)
        print(f"Graus dos vertices: {np.array(degree)}")

    #Verifica se o grafo é euleriano ou unicursal
    def graphEuleriano(self):
        degree = self.graph.sum(axis=0)
        euler = unicursal = 0

        for d in degree:
            if d % 2 == 0:
                euler += 1
            else:
                unicursal += 1

        if euler == len(degree):
            print('O grafo é Euleriano')
        elif unicursal == 2:
            print('O grafo é Unicursal')
        else:
            print('O grafo não é Euleriano nem Unicursal')




#Verifica se o grafo possui mais de um componentes
# if componentes == 0:
#     print('Grafo possui apenas um componente')
# elif componentes > 0:
#     print(f'Grafo possui {componentes} componentes')
