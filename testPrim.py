import sys 
import pandas as pd

class GraphPrim():
  
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)]
  
    def printPrim(self, parent):
        print ("Edge \tWeight")
        for i in range(1, self.v):
            print (f"{parent[i]} - {i} \t {self.graph[i][ parent[i]]}")
  

    def minKey(self, key, mstSet):
        min = sys.maxsize
  
        for v in range(self.v):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
  
        return min_index
  
    def prim(self):
        key = [sys.maxsize] * self.v
        parent = [None] * self.v 
        key[0] = 0 
        mstSet = [False] * self.v
  
        parent[0] = -1 
  
        for cout in range(self.v):
            u = self.minKey(key, mstSet)  
            mstSet[u] = True
  
            for v in range(self.v):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
  
        self.printPrim(parent)

if __name__ == "__main__":

    lista = pd.read_csv("assets/graphEnter.csv", sep=';', header=0, engine='python')

    g = GraphPrim(11)
    g.graph = lista.values
    
    g.prim()

