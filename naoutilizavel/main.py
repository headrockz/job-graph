from numpy import info
import pandas as pd
from graphs.heapMaximum import HeapMaximum
from graphs.dijkstra import AlgDijkstra
from assets import graphsMatrix as gm
from graphs.infoGraph import InfoGraph


def openListHeap():
    response = gm.with_weight
    newHeapMaximum = HeapMaximum()
    InfoGraph(response)

    # for i in response:
    #     for j in i:
    #         newHeapMaximum.add_nodes(j)

    # newHeapMaximum.view_heap()
    # removeElement = newHeapMaximum.removeNode()
    # print(f'The element removed was: {removeElement}')
    # newHeapMaximum.previewListHeapMaximun()

    # print('Dijkstra')

    # grafo = AlgDijkstra(7)

    # grafo.addEdge(1, 2, 5)
    # grafo.addEdge(1, 3, 6)
    # grafo.addEdge(1, 4, 10)
    # grafo.addEdge(2, 5, 13)
    # grafo.addEdge(3, 4, 3)
    # grafo.addEdge(3, 5, 11)
    # grafo.addEdge(3, 6, 6)
    # grafo.addEdge(4, 5, 6)
    # grafo.addEdge(4, 6, 4)
    # grafo.addEdge(5, 7, 3)
    # grafo.addEdge(6, 7, 8)

    # grafo.previewDisjktra()

    # result = grafo.disjktra(1)
    # print(result)

openListHeap()
