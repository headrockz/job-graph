grafo = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
]

def dfs(grafo, vertice):
    visitados = set()

    
    def dfs_iterativa(grafo, vertice_fonte):
        visitados.add(vertice_fonte)
        falta_visitar = [vertice_fonte]
        while falta_visitar:
            vertice = falta_visitar.pop()
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    falta_visitar.append(vizinho)
                    print(vizinho)

    dfs_iterativa(grafo, vertice)

dfs(grafo, grafo[0][0])
