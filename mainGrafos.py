def call_graph(choice='matriz'):
    if choice == 'matriz':
        #  chama  matriz
        print('mostrando a matrix')
    elif choice == 'lista':
        # chama lista
        print('mostrando a lista')

def call_alg(alg):
    if alg == '1' or alg.lower() == 'algoritmo 1':
        # chama algoritmo
        print('mostrando algoritmo 1')
    elif alg == '2' or alg.lower() == 'algoritmo 2':
        # chama algoritmo
        print('mostrando algoritmo 1')
    elif alg == '3' or alg.lower() == 'algoritmo 3':
        # chama algoritmo
        print('mostrando algoritmo 3')
    elif alg == '4' or alg.lower() == 'algoritmo 4':
        # chama algoritmo
        print('mostrando algoritmo 1')
    elif alg == '5' or alg.lower() == 'algoritmo 5':
        # chama algoritmo
        print('mostrando algoritmo 5')


def select_graphs():
    choice = input('''
[1] graph 1
[2] graph 2
[3] graph 3
[4] graph 4
[5] graph 5
escolha um grafo: ''')
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

    print('\n')
    viewGraph = input('''Visualizar grafo?
[1] Matrix de adjacencia
[2] lista
[0/N] Não visualizar
Digite sua escolha: ''')

    if viewGraph == '1' or viewGraph.lower() == 'matriz':
        call_graph('matriz')
    elif viewGraph == '2' or viewGraph.lower() == 'lista':
        call_graph('lista')
    else:
        print('não visualiza')

    input('\nPressione enter para escolher um dos algoritmos!')

    while True:
        alg = input('''
[1] algortimo 1
[2] algoritmo 2
[3] algoritmo 3
[4] algoritmo 4
[5] algortimo 5
[0/N] Para sair
Digite sua escolha: ''')
        # precisa trocar para os nomes dos algoritmos
        if alg == '1' or alg.lower() == 'algoritmo 1':
            call_alg(alg)

        else:
            print('Volte sempre!')
            break


select_graphs()
