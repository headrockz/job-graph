from .heapMinimum import HeapMinimum


class AlgDijkstra:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * self.vertices for i in range(self.vertices)]

    def add_egde(self, u, vertice, weight):
        self.graph[u - 1][vertice - 1] = weight
        self.graph[vertice - 1][u - 1] = weight

    def view_disjktra(self):
        print('Visualização da matriz')
        for i in range(self.vertices):
            print(self.graph[i])

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
                if self.graph[vertice - 1][i] != 0:
                    if result[i][0] == -1 or result[i][0] > distance + self.graph[vertice - 1][i]:
                        result[i] = [distance + self.graph[vertice - 1][i], vertice]
                        heapMinimum.add_nodes(distance + self.graph[vertice - 1][i], i + 1)
        return f'O melhor caminho é: \n{result}'


if __name__ == '__main__':
    graph = AlgDijkstra(11)

    graph.add_egde(1, 2, 7)
    graph.add_egde(1, 3, 4)
    graph.add_egde(1, 4, 6)
    graph.add_egde(2, 5, 6)
    graph.add_egde(2, 6, 2)
    graph.add_egde(3, 5, 4)
    graph.add_egde(3, 6, 4)
    graph.add_egde(4, 6, 4)
    graph.add_egde(4, 7, 2)
    graph.add_egde(5, 8, 4)
    graph.add_egde(5, 9, 1)
    graph.add_egde(6, 8, 2)
    graph.add_egde(6, 9, 5)
    graph.add_egde(6, 10, 4)
    graph.add_egde(7, 9, 3)
    graph.add_egde(7, 10, 4)
    graph.add_egde(8, 11, 4)
    graph.add_egde(9, 11, 5)
    graph.add_egde(10, 11, 4)

    graph.view_disjktra()

    result = graph.disjktra(1)
    print(f'\n{result}')
