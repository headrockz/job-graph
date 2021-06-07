'''
Caso execute esse algoritmo diretamente comente a linha 8 e descomente a linha 7
Pois como essa classe é chamada fora dessa pasta de algoritmos,  é necessario
colocar esse "." antes do nome do arquivo para o python entender que o arquivo
heapMinimum esta na mesma pasta que o arquivo dijkstra
'''
# from heapMinimum import HeapMinimum
from .heapMinimum import HeapMinimum
import pandas as pd


class AlgDijkstra:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * self.vertices for i in range(self.vertices)]

    def add_edge(self, origin, coming, weight):
        self.graph[origin][coming] = weight
        self.graph[coming][origin] = weight

    def view_dijkstra(self):
        print('Visualização da matriz')
        for i in range(self.vertices):
            print(self.graph[i])

    def dijkstra(self, origin):
       # minus one represents infinite | Origin
        result = [[-1, 0, 0] for i in range(self.vertices)]

        # Add value the origin
        result[origin - 1] = [0, origin, origin]

        # Starting heap minimum
        heapMinimum = HeapMinimum()

        # Add node the heap
        heapMinimum.add_nodes(0, origin)

        # Receiving the start heap, and verify which the minimum path
        while heapMinimum.size() > 0:
            distance, vertice = heapMinimum.remove_node()
            for i in range(self.vertices):
                if self.graph[vertice - 1][i] != 0:
                    if (result[i][0] == -1) or (result[i][0] > distance + self.graph[vertice - 1][i]):
                        result[i] = [distance + self.graph[vertice - 1][i], vertice, i+1]

                        heapMinimum.add_nodes(distance + self.graph[vertice - 1][i], i + 1)

       
        for k, v in enumerate(result):
            print(f'saindo do vertice: {v[1]}, indo para vertice {v[2]}, o custo atual é: {v[0]}')
        print(f'A menor distância do vertice {result[0][1]} até o vertice {result[-1][2]} é: {result[-1][0]}')


if __name__ == "__main__":
    graph = pd.read_csv("assets/graphEnter.csv", sep=';', header=0, engine='python')
    lista = graph.values
    
    g = AlgDijkstra(len(graph))


    for i in range(len(lista)):
        for j in range(len(lista[i])):
            g.add_egde(i, j, lista[i][j])


    g.view_matrix()

    g.disjktra(int(input("Digite o vertice de saida: ")))