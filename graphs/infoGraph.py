class InfoGraph:
    def __init__(self, graph):
        self.graph = graph
        self.degree = list()
        

    # Imprime o grafo
    def print_graph(self) -> None:

        for i in self.graph:
            for j in i:
                print(f'{j}', end=' ')
            
            print()

        print('=' * 50)

    # Numero de arestas
    def num_node(self) -> int:
        node = 0

        for i in self.graph:
            for j in i:
                if j != 0:
                    node += 1

        return round(node / 2)

    # Numero de vertices
    def num_vertice(self) -> int:
        vertice = len(self.graph)
        return vertice

    # Grau de cada vertice
    def num_degree(self) -> list:
        cont = 0
        for i in self.graph:
            for j in i:
                if j != 0:
                    cont += 1

            self.degree.append(cont)
            cont = 0

        return self.degree


    # Verifica se o grafo é euleriano ou unicursal
    def graph_euler(self) -> str:
        cont = 0

        for d in self.degree:
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
