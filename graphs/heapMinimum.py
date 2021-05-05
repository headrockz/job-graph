import math

class HeapMinimum:

    def __init__(self):
        # Starting nodes of the maximum heap function
        self.nodes = 0

        # Starting list with array empty
        self.listHeap = []

    def add_nodes(self, u, nodeAssociation):
        # Add value position end
        self.listHeap.append([u, nodeAssociation])

        # increment nodes
        self.nodes = self.nodes + 1

        # storing node child
        child = self.nodes

        # Enquanto form verdade
        while True:
            # if value is root, interrupts the function
            if child == 1:
                break

            # Fathe's position is equal to that of son divided by two (we use the whole part)
            father = child // 2

            # Father bigger than son; Stop
            if self.listHeap[father - 1][0] <= self.listHeap[child - 1][0]:
                break
            # Father less than son; switch position
            else:
                self.listHeap[father - 1], self.listHeap[child - 1] = self.listHeap[child - 1], self.listHeap[father - 1]
                child = father

    def remove_node(self):
        # Store temporary root node
        aux = self.listHeap[0]

        # Store root node the last node value
        self.listHeap[0] = self.listHeap[self.nodes - 1]

        # Remove last position
        self.listHeap.pop()

        # Remove one elements gives quantity node
        self.nodes = self.nodes - 1

        # Position start
        position = 1

        while True:
            # child the left
            child = 2 * position

            # If not child the left | not child the right
            if child > self.nodes:
                break

            # If child the right exist comper two child
            if child + 1 <= self.nodes:
                if self.listHeap[child][0] < self.listHeap[child - 1][0]:
                    child = child + 1

            # Compered child bigger with nodes
            if self.listHeap[position - 1][0] <= self.listHeap[child - 1][0]:
                break
            else:
                self.listHeap[child - 1], self.listHeap[position - 1] = self.listHeap[position - 1], self.listHeap[child - 1]
                position = child

        return aux

    def view_heap(self):
        #print(self.listHeap)

        print('A estrutura heap é:')

        # Identifying amount of nodes
        level = int(math.log(self.nodes, 2))

        aux = 0

        for i in range(level):
            for j in range( 2 ** i):
                print(f'{self.listHeap[aux]}', end=' ')
                aux = aux + 1
            print('')
        for i in range(self.nodes - aux):
            print(f'{self.listHeap[aux]}', end=' ')
            aux = aux + 1
        print('')

        #Mostra a raiz da arvore
    def root(self):
        print(f'O Nó raiz é {self.listHeap[0]}')
        
    def size(self):
        return self.nodes