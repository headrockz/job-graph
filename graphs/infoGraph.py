import numpy as np


class InfoGraph:
    def __init__(self, graph):
        self.graph = graph
        
        # print(self.printGraph())
        # print(f"Numero de vertices: {self.numVertice()}")
        # print(f"Numero de arestas: {self.numNode()}")
        # print(f"Graus dos vertices: {self.numDegree()}")
        # print(self.graphEuler())

    # Imprime o grafo
    def printGraph(self):
        return f'{self.graph}\n'

    # Numero de arestas
    def numNode(self):
        node = (self.graph.sum(axis=0).sum() / 2)
        return node

    # Numero de vertices
    def numVertice(self) -> int:
        vertice = len(self.graph)
        return vertice

    # Grau de cada vertice
    def numDegree(self):
        degree = self.graph.sum(axis=0)
        return np.array(degree)

    # Verifica se o grafo é euleriano ou unicursal
    def graphEuler(self):
        degree = self.graph.sum(axis=0)
        cont = 0

        for d in degree:
            if d % 2 != 0:
                cont += 1

        if cont == 0:
            return 'O grafo é Euleriano'
        elif cont == 2:
            return 'O grafo é Unicursal'
        else:
            return 'O grafo não é Euleriano nem Unicursal'


# Verifica se o grafo possui mais de um componentes
# if componentes == 0:
#     print('Grafo possui apenas um componente')
# elif componentes > 0:
#     print(f'Grafo possui {componentes} componentes')
