grafo = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'e'],
    'd': ['a', 'e'],
    'e': ['a', 'b', 'c', 'd', 'f'],
    'f': ['e']
}

def dfs(grafo, vertice):
    visitados = set()

    def dfs_iterativa(grafo, vertice_fonte):
        visitados.add(vertice_fonte)
        falta_visitar = [vertice_fonte]
        while falta_visitar:
            vertice = falta_visitar.pop()
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    print(vizinho)
                    visitados.add(vizinho)
                    falta_visitar.append(vizinho)

    dfs_iterativa(grafo, vertice)

dfs(grafo, 'b')
