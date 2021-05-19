import pandas as pd


graph = pd.read_csv("assets/weight.csv", sep=';', header=0, engine='python')


lista = graph.values
for i in range(len(lista)):
    # print('este é o I', i)
    for j in range(len(lista[i])):
        print(f'i: {i}, j: {j}, peso: {lista[i][j]}')