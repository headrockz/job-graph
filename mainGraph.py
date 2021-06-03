from time import sleep
import pandas as pd
from graphs.infoGraph import InfoGraph
from graphs.dijkstra import AlgDijkstra
from graphs.bellmanFord import BellmanFord
from graphs.bfs import GraphBfs


# Função para formatar uma mensagem
def massage(msg):
    print('=' * 50)
    print(f"{msg:^50}")
    print('=' * 50)



# Função para escolher o algoritmo
def call_alg(alg, graph):
    lista = graph.values
    
    if alg == '1':
        g = AlgDijkstra(aux.num_vertice())
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                g.add_edge(i, j, lista[i][j])

        g.dijkstra(int(input("Digite o vertice de saida: ")))
        sleep(1)
    elif alg == '2':
        g = BellmanFord(aux.num_vertice())
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                g.add_edge(i, j, lista[i][j])
        
        g.bellman_ford(int(input("Digite o vertice de saida: ")))     
        sleep(1)
    elif alg == '3':
        g = GraphBfs()
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j] != 0:
                    g.add_edge(i, j)

        g.BFS(int(input("Digite o vertice de saida: "))) 
        sleep(1)
    elif alg == '4':
        sleep(1)
        # chama algoritmo(graph)
        print('mostrando algoritmo 4')
    else:
        print('')


# Finção para escolher o grafo
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


# Função principal
while True:
    massage('Escolha um Grafo')
    choice = input('[1] Grafo 1 - K5\n'
                    '[2] Grafo 2 - n3e2\n'
                    '[3] Grafo 3 - n4e5\n'
                    '[4] Grafo 4 - weight\n'
                    '[5] Grafo 5 - Grafo que o usuario entrou\n'
                    'Digite sua escolha: ')

    graph = choice_graph(choice)
    
    view = input('Visualizar grafo? [S/n]: ')
    aux = InfoGraph(graph.values)
    
    if  view not in 'nN':
        massage('Matriz de Adjacências')
        # Mostrando informações sobre o grafo    
        aux.print_graph()
        print(f"Numero de vertices: {aux.num_vertice()}")
        print(f"Numero de arestas: {aux.num_node()}")
        print(f"Graus dos vertices: {aux.num_degree()}")
        print(aux.graph_euler())
    
    outher = input('Deseja escolher outro grafo? [s/N]: ')
    if outher not in 'sS':
        break

while True:
    massage('Escolha um Algoritmo')
    alg = input('[1] dijkstra\n'
                '[2] bellman ford\n'
                '[3] bfs\n'
                '[4] algoritmo 4\n'
                '[0/N] Para sair\n'
                'Digite sua escolha: ')

    print('')
    call_alg(alg, graph)
    
    if alg == '0' or alg.lower() == 'n':
        massage('Volte sempre!')
        break
