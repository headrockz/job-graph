import pandas as pd


class BellmanFord:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        if w != 0:
            self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertice, distancia ate o vertice de saida")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

    def bellman_ford(self, src):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)


if __name__ == "__main__":
    graph = pd.read_csv("assets/graphEnter.csv", sep=';', header=0, engine='python')
    lista = graph.values

    g = BellmanFord(len(graph))

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            g.add_edge(i, j, lista[i][j])

    g.bellman_ford(int(input("Digite o vertice de saida: "))) 
