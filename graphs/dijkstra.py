from .heapMinimum import HeapMinimum


class Dijkstra:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def addEdge(self, u, vertice, weight):
        self.grafo[u - 1][vertice - 1] = weight
        self.grafo[vertice - 1][u - 1] = weight

    def previewDisjktra(self):
        print('Preview matrice Djktra')
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
        heapMinimum.addNodes(0, origin)

        # Receiving the start heap, and verify which the minimum path
        while heapMinimum.size() > 0:
            distance, vertice = heapMinimum.removeNode()
            for i in range(self.vertices):
                if self.grafo[vertice - 1][i] != 0:
                    if result[i][0] == -1 or result[i][0] > distance + self.grafo[vertice - 1][i]:
                        result[i] = [distance + self.grafo[vertice - 1][i], vertice]
                        heapMinimum.addNodes(distance + self.grafo[vertice - 1][i], i + 1)
        return result


grafo = Dijkstra(7)

grafo.addEdge(1, 2, 5)
grafo.addEdge(1, 3, 6)
grafo.addEdge(1, 4, 10)
grafo.addEdge(2, 5, 13)
grafo.addEdge(3, 4, 3)
grafo.addEdge(3, 5, 11)
grafo.addEdge(3, 6, 6)
grafo.addEdge(4, 5, 6)
grafo.addEdge(4, 6, 4)
grafo.addEdge(5, 7, 3)
grafo.addEdge(6, 7, 8)

grafo.previewDisjktra()

result = grafo.disjktra(1)
print(result)
