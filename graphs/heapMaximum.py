import math


class HeapMaximum:
    def __init__(self):
        # Starting nodes of the maximum heap function
        self.nodes = 0
        # Starting list with array empty
        self.listHeap = []

    def add_nodes(self, u):
        # Add value position end
        self.listHeap.append(u)

        # increment nodes
        self.nodes = self.nodes + 1

        # storing node child
        child = self.nodes

        # Enquanto for verdade
        while True:
            # if value is root, interrupts the function
            if child == 1:
                break

            # Fathe's position is equal to that of son divided by two (we use the whole part)
            father = child // 2

            # Father bigger than son; Stop
            if self.listHeap[father - 1] >= self.listHeap[child - 1]:
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
                if self.listHeap[child] > self.listHeap[child - 1]:
                    child = child + 1

            # Compered child bigger with nodes
            if self.listHeap[position - 1] >= self.listHeap[child - 1]:
                break
            else:
                self.listHeap[child - 1], self.listHeap[position - 1] = self.listHeap[position - 1], self.listHeap[child - 1]
                position = child

        return aux

    def view_heap(self):
        # print(self.listHeap)

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

    #Mostra a raiz da arvore
    def root(self):
        print(f'O Nó raiz é {self.listHeap[0]}')

    #Mostra a tamanho da arvore
    def size(self):
        return self.nodes


if __name__ == '__main__':
    h = HeapMaximum()

    h.add_nodes(17)
    h.add_nodes(36)
    h.add_nodes(25)
    h.add_nodes(7)
    h.add_nodes(3)
    h.add_nodes(100)
    h.add_nodes(1)
    h.add_nodes(2)
    h.add_nodes(19)

    h.view_heap()
    h.root()