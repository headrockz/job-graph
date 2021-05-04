import numpy as np


class InfoGraph:
    def __init__(self, graph):
        self.graph = graph
        
        self.printGraph()
        self.numVertice()
        self.numArrest()
        self.numDegree()
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
        cont = 0

        for d in degree:
            if d % 2 != 0:
                cont += 1

        if cont == 0:
            print('O grafo é Euleriano')
        elif cont == 2:
            print('O grafo é Unicursal')
        else:
            print('O grafo não é Euleriano nem Unicursal')


#Verifica se o grafo possui mais de um componentes
# if componentes == 0:
#     print('Grafo possui apenas um componente')
# elif componentes > 0:
#     print(f'Grafo possui {componentes} componentes')
