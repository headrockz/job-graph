import pandas as pd


class HeapMinimum:
    def __init__(self):
        # Starting nodes of the maximum heap function
        self.nodes = 0

        # Starting list with array empty
        self.listHeap = []

    def add_nodes(self, u, nodeAssociation):
        # Add value position end
        self.listHeap.append([u, nodeAssociation])

        # increment nodes
        self.nodes = self.nodes + 1

        # storing node child
        child = self.nodes

        # Enquanto form verdade
        while True:
            # if value is root, interrupts the function
            if child == 1:
                break

            # Fathe's position is equal to that of son divided by two (we use the whole part)
            father = child // 2

            # Father bigger than son; Stop
            if self.listHeap[father - 1][0] <= self.listHeap[child - 1][0]:
                break
            # Father less than son; switch position
            else:
                self.listHeap[father - 1], self.listHeap[child - 1] = self.listHeap[child - 1], self.listHeap[father - 1]
                child = father

    def remove_node(self):
        # Store temporary root node
        aux = self.listHeap[0]

        # Store root node the last node value
        self.listHeap[0] = self.listHeap[self.nodes - 1]

        # Remove last position
        self.listHeap.pop()

        # Remove one elements gives quantity node
        self.nodes = self.nodes - 1

        # Position start
        position = 1

        while True:
            # child the left
            child = 2 * position

            # If not child the left | not child the right
            if child > self.nodes:
                break

            # If child the right exist comper two child
            if child + 1 <= self.nodes:
                if self.listHeap[child][0] < self.listHeap[child - 1][0]:
                    child = child + 1

            # Compered child bigger with nodes
            if self.listHeap[position - 1][0] <= self.listHeap[child - 1][0]:
                break
            else:
                self.listHeap[child - 1], self.listHeap[position - 1] = self.listHeap[position - 1], self.listHeap[child - 1]
                position = child

        return aux


    def size(self):
        return self.nodes


class AlgDijkstra:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * self.vertices for i in range(self.vertices)]
        

    def add_egde(self, u, vertice, weight):
        self.graph[u][vertice] = weight
        self.graph[vertice][u] = weight

    def view_matrix(self):
        print('Visualização da matriz')
        for i in range(self.vertices):
            print(self.graph[i])

    def disjktra(self, origin) -> None:
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
            # print(f'a distancia {distance} vertice {vertice}')
            for i in range(self.vertices):
                if self.graph[vertice - 1][i] != 0:
                    if (result[i][0] == -1) or (result[i][0] > distance + self.graph[vertice - 1][i]):
                        result[i] = [distance + self.graph[vertice - 1][i], vertice, i+1]

                        heapMinimum.add_nodes(distance + self.graph[vertice - 1][i], i + 1)

        for k, v in enumerate(result):
            print(f'saindo do vertice: {v[1]}, indo para vertice {v[2]}, o custo atual é: {v[0]}')
        print(f'A menor distância é: {result[-1][0]}')


g = AlgDijkstra(7)

graph = pd.read_csv("assets/weight.csv", sep=';', header=0, engine='python')

lista = graph.values
for i in range(len(lista)):
    for j in range(len(lista[i])):
        g.add_egde(i, j, lista[i][j])


# g.view_matrix()

g.disjktra(1)

