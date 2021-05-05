from heapMinimum import HeapMinimum


class AlgDijkstra:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def add_egde(self, u, vertice, weight):
        self.grafo[u - 1][vertice - 1] = weight
        self.grafo[vertice - 1][u - 1] = weight

    def view_disjktra(self):
        print('Visualização da matriz')
        for i in range(self.vertices):
            print(self.grafo[i])

    def disjktra(self, origin):
        # minus one represents infinite | Origin
        result = [[-1, 0] for i in range(self.vertices)]

        # Add value the origin
        result[origin - 1] = [0, origin]

        # Starting heap minimum
        heapMinimum = HeapMinimum()

        # Add node the heap
        heapMinimum.add_nodes(0, origin)

        # Receiving the start heap, and verify which the minimum path
        while heapMinimum.size() > 0:
            distance, vertice = heapMinimum.remove_node()
            for i in range(self.vertices):
                if self.grafo[vertice - 1][i] != 0:
                    if result[i][0] == -1 or result[i][0] > distance + self.grafo[vertice - 1][i]:
                        result[i] = [distance + self.grafo[vertice - 1][i], vertice]
                        heapMinimum.add_nodes(distance + self.grafo[vertice - 1][i], i + 1)
        return f'O melhor caminho é: \n{result}'


grafo = AlgDijkstra(7)

grafo.add_egde(1, 2, 5)
grafo.add_egde(1, 3, 6)
grafo.add_egde(1, 4, 10)
grafo.add_egde(2, 5, 13)
grafo.add_egde(3, 4, 3)
grafo.add_egde(3, 5, 11)
grafo.add_egde(3, 6, 6)
grafo.add_egde(4, 5, 6)
grafo.add_egde(4, 6, 4)
grafo.add_egde(5, 7, 3)
grafo.add_egde(6, 7, 8)

grafo.view_disjktra()

result = grafo.disjktra(1)
print(f'\n{result}')
