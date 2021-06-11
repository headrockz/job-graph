from time import sleep
import pandas as pd
from graphs.infoGraph import InfoGraph
from graphs.dijkstra import GraphDijkstra
from graphs.bellmanFord import BellmanFord
from graphs.bfs import GraphBfs
from graphs.krustal import GraphKrustal


def massage(msg):
    print('=' * 62)
    print(f"{msg:^62}")
    print('=' * 62)


def call_alg(alg, graph):
    graph = graph.values
    
    if alg == '1':
        g = GraphDijkstra(aux.num_vertice())
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                g.add_edge(i, j, graph[i][j])

        print('PS: lembre-se que nesse algoritmo pela implementação a matriz começa do 1 e NÃO do 0')
        g.dijkstra(int(input("Digite o vertice de saida: ")))
        sleep(1)
    elif alg == '2':
        g = BellmanFord(aux.num_vertice())
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                g.add_edge(i, j, graph[i][j])
        
        print('PS: lembre-se que nesse algoritmo pela implementação a matriz começa do 0')
        g.bellman_ford(int(input("Digite o vertice de saida: ")))     
        sleep(1)
    elif alg == '3':
        g = GraphBfs()
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] != 0:
                    g.add_edge(i, j)

        print('PS: lembre-se que nesse algoritmo pela implementação a matriz começa do 0')
        g.BFS(int(input("Digite o vertice de saida: "))) 
        sleep(1)
    elif alg == '4':
        g = GraphKrustal(aux.num_vertice())

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                g.add_edge(i, j, graph[i][j])
    
        g.kruskal()
        sleep(1)
    else:
        print('')


def choice_graph(choice):
    if choice == '1':
        graph = pd.read_csv("assets/K5.csv", sep=';', header=0, engine='python')
    elif choice == '2':
        # graph = graph2
        graph = pd.read_csv("assets/n3e2.csv", sep=';', header=0, engine='python')
    elif choice == '3':
        graph = pd.read_csv("assets/n4e5.csv", sep=';', header=0, engine='python')
    elif choice == '4':
        graph = pd.read_csv("assets/weight.csv", sep=';', header=0, engine='python')
    elif choice == '5':
        graph = pd.read_csv("assets/graphEnter.csv", sep=';', header=0, engine='python')
    
    return graph

   
while True:
    massage('Escolha um Grafo')
    choice = input('[1] Grafo 1 - K5\n'
                    '[2] Grafo 2 - n3e2\n'
                    '[3] Grafo 3 - n4e5\n'
                    '[4] Grafo 4 - weight\n'
                    '[5] Grafo 5 - Grafo que o usuario entrou no arquivo graphEnter\n'
                    'Digite sua escolha: ')

    graph = choice_graph(choice)
    aux = InfoGraph(graph.values)
    
    view = input('Visualizar grafo? [S/n]: ')
    
    if view in 'nN':
        massage('Matriz de Adjacências')
         
        aux.print_graph()
        print(f"Numero de vertices: {aux.num_vertice()}")
        print(f"Numero de arestas: {aux.num_node()}")
        print(f"Graus dos vertices: {aux.num_degree()}")
        print(aux.graph_euler())
    
        outher = input('Deseja escolher outro grafo? [s/N]: ')
        if outher in 'sS':
            break

while True:
    massage('Escolha um Algoritmo')
    alg = input('[1] dijkstra\n'
                '[2] bellman ford\n'
                '[3] BFS\n'
                '[4] Krustal\n'
                '[0/N] Para sair\n'
                'Digite sua escolha: ')

    print('')
    call_alg(alg, graph)
    
    if alg == '0' or alg in 'nN':
        massage('Volte sempre!')
        break
