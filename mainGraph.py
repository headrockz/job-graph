from time import sleep
import pandas as pd
# import numpy as np
from graphs.infoGraph import InfoGraph


# Função para escolher a visualização da matriz ou lista
def call_view(choice, graph):
    print('')

    if choice == '1':
        massage('Matriz de Adjacências')
        # Mostrando informações sobre o grafo    
        InfoGraph(graph)
    elif choice == '2':
        # chama lista
        print('mostrando a lista')



# Função para escolher o algoritmo
def call_alg(alg, graph):
    if alg == '1':
        # chama algoritmo(graph)
        print('mostrando algoritmo 1')
    elif alg == '2':
        # chama algoritmo(graph)
        print('mostrando algoritmo 2')
    elif alg == '3':
        # chama algoritmo(graph)
        print('mostrando algoritmo 3')
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
[4] Grafo 4 -
[5] Grafo 5 -
Digite sua escolha: ''')

    if choice == '1':
        graph = pd.read_csv("assets/K5.csv", sep=';', header=0, engine='python')
    elif choice == '2':
        # graph = graph2
        graph = pd.read_csv("assets/n3e2.csv", sep=';', header=0, engine='python')
    elif choice == '3':
        graph = pd.read_csv("assets/n4e5.csv", sep=';', header=0, engine='python')
    elif choice == '4':
        # graph = graph 4
        print('grafo 4')
    else:
        # graph = graph5
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
[1] algortimo 1
[2] algoritmo 2
[3] algoritmo 3
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
