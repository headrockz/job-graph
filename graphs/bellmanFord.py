import pandas as pd


class BellmanFord:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [] 


    def add_edge(self, s, d, w):
        if w != 0:
            self.graph.append([s, d, w])


    def print_solution(self, dist):
        print("Vertice, distancia ate o vertice de saida")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

    def bellman_ford(self, src):

        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w


        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(dist)


if __name__ == "__main__":
    # Area de teste do algorimo

    # Entre com seu grafo no arquivo graphEnter.csv
    graph = pd.read_csv("assets/graphEnter.csv", sep=';', header=0, engine='python')
    lista = graph.values

    g = BellmanFord(len(graph))

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            g.add_edge(i, j, lista[i][j])

    print('PS: lembre-se que nesse algoritmo pela implementação a matriz começa do 0')
    g.bellman_ford(int(input("Digite o vertice de saida: "))) 
