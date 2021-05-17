grafo = {
    1: [2, 4, 5],
    2: [1, 3, 5],
    3: [2, 5],
    4: [1, 5],
    5: [1, 2, 3, 4, 6],
    6: [5]
}

# coisos globais
valor_profundidade_entrada = 0 # contador da profundidade em que os vertices entram da pilha (chamado recursivamente)
valor_profundidade_saida = 0 # contador da profundidade em que os vertices saem da pilha (termina sua chamada recursiva)
# dicionario com as profunfidades em que cada vertice entrou e saiu da pilha numa lista [profundidade_entrada, profundidade_saida]
profundidades_entrada_saida = {}
pai = {} # dicionario com os pais de cada vertice na arvore de busca em profundidade
aresta = {} # classificacao das arestas na arvore de busca em profundidade do grafo
niveis = {} # nivel de cada vertice na arvore de busca em profundidade
# o low eh o vertice mais proximo da raiz da arvore de busca em profundidade que consigo chegar descendo pelas arestas de arvore quantas vezes eu queira (incluindo 0 vezes) e subindo uma unica vez por uma aresta de retorno
low = {}
# um demarcador eh um vertice que tem como low seu pai ou ele mesmo
demarcadores = set()
# uma articulacao eh um vertice que, caso seja removido do grafo (junto com suas arestas associadas) torna-o desconexo
articulacoes = set()

# funcao de chamada
def busca_em_profundidade(grafo, vertice_do_grafo):
    # todos os vertices do grafo comecam achando que eles mesmos sao seus lows
    for vertice in grafo:
        low[vertice] = vertice

    pai[vertice_do_grafo] = None # a raiz naum tem pai
    qtd_filhos_da_raiz = call_to_busca_em_profundidade(grafo, vertice_do_grafo, 1)
    # (*) concertando a raiz:
    if qtd_filhos_da_raiz <= 1:
        # se a raiz soh tem um filho, significa que esse vertice, no grafo original, soh estah ligado a vertices que jah possuem um outro caminho entre eles que naum passa pela raiz, e portanto ela naum se trata de uma articulacao, pois remove-la naum desconectarah o grafo
        articulacoes.remove(vertice_do_grafo)

# funcao recursiva
def call_to_busca_em_profundidade(grafo, vertice_do_grafo, nivel):
    global valor_profundidade_entrada, valor_profundidade_saida
    valor_profundidade_entrada += 1 # atualizando o contador de profundidade de entrada
    profundidades_entrada_saida[vertice_do_grafo] = [valor_profundidade_entrada, None] # anotando profundidade de entrada de vertice_do_grafo
    niveis[vertice_do_grafo] = nivel # anotando o nivel desse vertice_do_grafo na arvore de busca em profundidade

    count_filhos = 0 # contador de filhos do vertice por arestas de arvore que soh serah usado pela busca_em_profundidade (chamada da raiz) para concertar a raiz caso ela tenha sido escolhida como articulacao erroneamente

    for vizinho in grafo.get(vertice_do_grafo): # percorrendo os vizinhos de vertice_do_grafo
        # (descomente os codigos abaixo para ver a ordem em que as arestas sao visitadas e suas respectivas classificacoes)
        print('%s -> %s:' % (str(vertice_do_grafo), str(vizinho)))
        if not profundidades_entrada_saida.get(vizinho): # testa se esse vizinho jah foi empilhado (chamado pela recursao)
            # se ainda naum foi empilhado, eh hora de...
            pai[vizinho] = vertice_do_grafo # ... atualizar quem eh o pai dele na arvore de busca em profundidade
            # MOMENTO PARA VISITAR vertice_do_grafo -> vizinho COMO ARESTA DE ARVORE
            count_filhos += 1 # contando a quantidade de filhos do vertice por arestas de arvore (esse valor soh serah relevante para a raiz (primeira chamada de call_to_busca_em_profundidade feita por busca_em_profundidade))
            # aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
            # print('aresta de arvore')
            # chamada de recursao escolhendo agora esse vizinho como raiz:
            call_to_busca_em_profundidade(grafo, vizinho, nivel + 1) # o proximo vertice estarah um nivel abaixo desse na arvore de busca em profundidade
            # HORA DE TESTAR SE O MEU FILHO TEM UM LOW MELHOR QUE O MEU!
            if niveis[low[vizinho]] < niveis[low[vertice_do_grafo]]: # caso meu filho tenha um low melhor que o meu...
                low[vertice_do_grafo] = low[vizinho] # atualizo o meu low, para o low do meu filho (afinal podemos descer quantas vezes quisermos por arestas de arvore para achar o low, lembram?)
            # NESSE MOMENTO EU JAH SEI SE MEUS FILHOS SAO DEMARCADORES OU NAUM!
            if vizinho in demarcadores:
                # se esse vertice_do_grafo eh pai de um demarcador na arvore de busca em profundidade, entao ele eh uma articulacao!
                articulacoes.add(vertice_do_grafo) # repare que nesse momento, podemos ter sujado o vertice escolhido como raiz da busca, pois pode se tratar de um vertice que "fica nas extremidades do grafo", vamos concertar isso em (*)
        else: # caso o vizinho jah esteja na pilha (jah houve uma chamada de call_to_busca_em_profundidade com parametro vertice_do_grafo=vizinho)
            # testa se esse vizinho jah foi desempilhado (terminou sua chamada de call_to_busca_em_profundidade)
            if not profundidades_entrada_saida[vizinho][1]:
                if pai[vertice_do_grafo] != vizinho: # testando se o vizinho eh o pai do vertice tratado nessa chamada de call_to_busca_em_profundidade
                    # caso o vizinho naum seja o pai do vertice dessa chamada de call_to_busca_em_profundidade, eh hora de...
                    # MOMENTO PARA VISITAR vertice_do_grafo -> vizinho COMO ARESTA DE RETORNO
                    # aresta[(vertice_do_grafo, vizinho)] = 'aresta de retorno'
                    # print('aresta de retorno')
                    # por se tratar de uma aresta de retorno, pode ser que meu vizinho esteja mais proximo da raiz que o meu low...
                    if niveis[vizinho] < niveis[low[vertice_do_grafo]]:
                        low[vertice_do_grafo] = vizinho # ... nesse caso, atualizo meu low
                else:
                    aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
                    print('aresta de arvore')
            else:
                aresta[(vertice_do_grafo, vizinho)] = 'aresta de arvore'
                print('aresta de arvore')

    valor_profundidade_saida += 1 # atualizando o contador de profundidade de saida
    profundidades_entrada_saida[vertice_do_grafo][1] = valor_profundidade_saida
    # NESSE MOMENTO EU SEI SE ESSE vertice_do_grafo EH UM DEMARCADOR OU NAUM!
    if low[vertice_do_grafo] in (vertice_do_grafo, pai[vertice_do_grafo]): # se meu low sou eu mesmo ou meu pai...
        demarcadores.add(vertice_do_grafo) # ... entao eu sou um demarcador!

    return count_filhos


busca_em_profundidade(grafo, 1)
