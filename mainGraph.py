from time import sleep
import pandas as pd
import numpy as np


graph = pd.read_csv("assets/K5.csv", sep=';', header=None, engine='python')


def call_graph(choice):
    #Função para escholer o grafo
    # precisa trocar para os nomes dos grafos
    if choice == '1' or choice.lower() == 'graph 1':
        # graph = graph1
        print('graph 1')
    elif choice == '2' or choice.lower() == 'graph 2':
        # graph = graph2
        print('grafo 2')
    elif choice == '3' or choice.lower() == 'graph 3':
        # graph = graph3
        print('grafo 3')
    elif choice == '4' or choice.lower() == 'graph 4':
        # graph = graph 4
        print('grafo 4')
    else:
        # graph = graph5
        print('grafo 5')


def call_view(choice):
    #Função para escolher a visualização da matriz ou lista
    print('')

    if choice == '1':
        #Mostrando A matriz
        print('Matriz de Adjacências\n')
        print(graph)
        print('')
        
        #Numero de vertices
        numeroVertices = len(graph)
        print("Numero de vertices:", numeroVertices)

        #Numero de arestas
        numeroArestas = (graph.sum(axis=0).sum() / 2)
        print("Numero de arestas:", int(numeroArestas))

        #Grau de cada vertice
        grausVertices = graph.sum(axis=0)
        print("Graus dos vertices:", np.array(grausVertices))

    elif choice == '2':
        # chama lista
        print('mostrando a lista')



def call_alg(alg):
    #Função para escolher o algoritmo
    if alg == '1':
        # chama algoritmo
        print('mostrando algoritmo 1')
    elif alg == '2':
        # chama algoritmo
        print('mostrando algoritmo 1')
    elif alg == '3':
        # chama algoritmo
        print('mostrando algoritmo 3')
    elif alg == '4':
        # chama algoritmo
        print('mostrando algoritmo 1')
    elif alg == '5':
        # chama algoritmo
        print('mostrando algoritmo 5')
    else:
        print('')
        massage('Volte sempre!')


def massage(msg):
    #Função para Formatar uma mensagem
    print('=' * 50)
    print(f"{msg:^50}")
    print('=' * 50)


def main():
    #Função principal
    massage('Escolha um Grafo')
    choice = input('''
[1] graph 1
[2] graph 2
[3] graph 3
[4] graph 4
[5] graph 5
Digite sua escolha: ''')

    call_graph(choice)
    sleep(0.5)

    print('')

    massage('Visualizar grafo?')

    viewGraph = input('''
[1] Matriz
[2] lista
[0/N] Não visualizar
Digite sua escolha: ''')

    call_view(viewGraph)

    input('Pressione enter para escolher um dos algoritmos!')

    while True:
        print('\n')
        massage('Eschola um Algoritmo')
        alg = input('''
[1] algortimo 1
[2] algoritmo 2
[3] algoritmo 3
[4] algoritmo 4
[5] algortimo 5
[0/N] Para sair
Digite sua escolha: ''')
        # precisa trocar para os nomes dos algoritmos
        call_alg(alg)
        
        if alg == '0' or alg.lower() == 'n':
            break

        sleep(1)


main()
