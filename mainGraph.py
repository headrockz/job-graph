from time import sleep
import pandas as pd
from graphs.infoGraph import InfoGraph
from graphs.dijkstra import AlgDijkstra
from graphs.bellmanFord import BellmanFord
from graphs.bfs import GraphBfs


# Função para escolher a visualização da matriz ou lista
def call_view(choice, graph):
    print('')

    if choice == '1':
        massage('Matriz de Adjacências')
        # Mostrando informações sobre o grafo    
        aux = InfoGraph(graph)
        print(aux.printGraph())
        print(f"Numero de vertices: {aux.numVertice()}")
        print(f"Numero de arestas: {aux.numNode()}")
        print(f"Graus dos vertices: {aux.numDegree()}")
        print(aux.graphEuler())
    elif choice == '2':
        # chama lista
        print('mostrando a lista')



# Função para escolher o algoritmo
def call_alg(alg, graph):
    aux = InfoGraph(graph)
    lista = graph.values
    
    if alg == '1':
        g = AlgDijkstra(aux.numVertice())
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                g.add_edge(i, j, lista[i][j])

        g.view_disjktra()
        print(g.disjktra(int(input("Digite o vertice de saida: "))))

    elif alg == '2':
        g = BellmanFord(aux.numVertice())
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                g.add_edge(i, j, lista[i][j])
        
        g.bellman_ford(int(input("Digite o vertice de saida: ")))
        
    elif alg == '3':
        g = GraphBfs()
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                if lista[i][j] != 0:
                    g.addEdge(i, j)

        print ("Segue a execução do BFS, começando pelo vértice 2")
        g.BFS(int(input("Digite o vertice de saida: "))) 

    elif alg == '4':
        # chama algoritmo(graph)
        print('mostrando algoritmo 4')
    elif alg == '5':
        # chama algoritmo(graph)
        print('mostrando algoritmo 5')
    else:
        print('')


# Função para formatar uma mensagem
def massage(msg):
    print('=' * 50)
    print(f"{msg:^50}")
    print('=' * 50)


# Função principal
def main():
    massage('Escolha um Grafo')
    choice = input('''
[1] Grafo 1 - K5
[2] Grafo 2 - n3e2
[3] Grafo 3 - n4e5
[4] Grafo 4 - weight
[5] Grafo 5 - TEST
Digite sua escolha: ''')

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
        graph = pd.read_csv("assets/test.csv", sep=';', header=0, engine='python')
        print('grafo 5')
    
    sleep(0.5)

    print('')

    massage('Visualizar grafo?')

    viewGraph = input('''
[1] Matriz de Adjacência
[2] lista
[0/N] Não visualizar
Digite sua escolha: ''')

    call_view(viewGraph, graph)

    input('\nPressione enter para escolher um dos algoritmos!')

    while True:
        print('\n')
        massage('Escolha um Algoritmo')
        # precisa trocar para os nomes dos algoritmos
        alg = input('''
[1] dijkstra
[2] bellman ford
[3] bfs
[4] algoritmo 4
[5] algortimo 5
[0/N] Para sair
Digite sua escolha: ''')

        call_alg(alg, graph)
        
        if alg == '0' or alg.lower() == 'n':
            massage('Volte sempre!')
            break

        sleep(1)


main()
