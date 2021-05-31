import pandas as pd

def numNode(graph) -> int:
    node = 0

    for i in graph:
        for j in i:
            if j != 0:
                node += 1

    return round(node / 2)


def numDegree(graph) -> list:
    cont = 0
    degree = list()
    for i in graph:
        for j in i:
            if j != 0:
                cont += 1

        degree.append(cont)
        cont = 0

    return degree


graph = pd.read_csv("assets/weight.csv", sep=';', header=0, engine='python')
print(numNode(graph.values))
print(numDegree(graph.values))