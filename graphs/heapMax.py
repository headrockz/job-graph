from math import log

class HeapMax:
    def __init__(self):
        self.nodes = 0
        self.listHeap = []

    def add_node(self, u):
        self.listHeap.append(u)
        self.nodes += 1
        child = self.nodes

        while True:
            if child == 1:
                break
                
            father = child // 2

            if self.listHeap[father-1] >= self.listHeap[child-1]:
                break
            else:
                self.listHeap[father-1], self.listHeap[child-1] = self.listHeap[child-1], self.listHeap[father-1]
                child = father
        
    def remove_node(self):
        aux = self.listHeap[0]
        self.listHeap[0] = self.listHeap[self.nodes-1]
        self.listHeap.pop()
        self.nodes -= 1

        position = 1

        while True:
            pass

    def view_heap(self):
        #Forma simples de se mostrar a heap
        # print(self.listHeap)

        print('A estrutura heap é:')

        level = int(log(self.nodes, 2)) 
        aux = 0

        for i in range(level):
            for j in range(2 ** i):
                print(f'{self.listHeap[aux]}', end=' ')
                aux += 1

            print('')

            for i in range(self.nodes - aux):
                print(f'{self.listHeap[aux]}', end=' ')
                aux += 1
        

h = HeapMax()

h.add_node(17)
h.add_node(36)
h.add_node(25)
h.add_node(7)
h.add_node(3)
h.add_node(100)
h.add_node(1)
h.add_node(2)
h.add_node(19)

h.view_heap()