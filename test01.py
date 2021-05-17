import pandas as pd


graph = pd.read_csv("assets/Kpeso.csv", sep=';', header=0, engine='python')


lista = graph.values
for i in range(len(lista)):
    # print('este é o I', i)
    for j in range(len(lista[i])):
        print('este é o j', lista[i][j])