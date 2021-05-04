import pandas as pd
import numpy as np


matrix = pd.read_csv("assets/K5.csv", sep=';', header=None, engine='python')
numeroVertices = len(matrix)


class Graph:
    def __init__(self, vertices, matrix):
        self.vertices = vertices
        self.matrix = matrix
    
    def imprime(self):
        print(self.vertices)
        print(self.matrix)


graph = Graph(numeroVertices, matrix)
graph.imprime()