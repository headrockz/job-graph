import math

class HeapMinimum:

    def __init__(self):
        # Starting nodes of the maximum heap function
        self.nodes = 0

        # Starting list with array empty
        self.listHeapMaximum = []

    def addNodes(self, u, nodeAssociation):
        # Add value position end
        self.listHeapMaximum.append([u, nodeAssociation])

        # increment nodes
        self.nodes = self.nodes + 1

        # storing node child
        childerNodes = self.nodes

        # Enquanto form verdade
        while True:
            # if value is root, interrupts the function
            if childerNodes == 1:
                break

            # Fathe's position is equal to that of son divided by two (we use the whole part)
            primaryNodes = childerNodes // 2

            # Father bigger than son; Stop
            if self.listHeapMaximum[primaryNodes - 1][0] <= self.listHeapMaximum[childerNodes - 1][0]:
                break
            # Father less than son; switch position
            else:
                self.listHeapMaximum[primaryNodes - 1], self.listHeapMaximum[childerNodes - 1] = self.listHeapMaximum[childerNodes - 1], self.listHeapMaximum[primaryNodes - 1]
                childerNodes = primaryNodes

    def removeNode(self):
        # Store temporary root node
        nodeTemp = self.listHeapMaximum[0]

        # Store root node the last node value
        self.listHeapMaximum[0] = self.listHeapMaximum[self.nodes - 1]

        # Remove last position
        self.listHeapMaximum.pop()

        # Remove one elements gives quantity node
        self.nodes = self.nodes - 1

        # Position start
        position = 1

        while True:
            # Childer the left
            childer = 2 * position

            # If not childer the left | not childer the right
            if childer > self.nodes:
                break

            # If childer the right exist comper two childer
            if childer + 1 <= self.nodes:
                if self.listHeapMaximum[childer][0] < self.listHeapMaximum[childer - 1][0]:
                    childer = childer + 1

            # Compered childer bigger with nodes
            if self.listHeapMaximum[position - 1][0] <= self.listHeapMaximum[childer - 1][0]:
                break
            else:
                self.listHeapMaximum[childer - 1], self.listHeapMaximum[position - 1] = self.listHeapMaximum[position - 1], self.listHeapMaximum[childer - 1]
                position = childer

        return nodeTemp

    def previewListHeapMaximun(self):
        #print(self.listHeapMaximum)

        print('The structure heap')

        # Identifying amount of nodes
        level = int(math.log(self.nodes, 2))

        nodeTemp = 0

        for i in range(level):
            for j in range( 2 ** i):
                print(f'{self.listHeapMaximum[nodeTemp]}', end=' ')
                nodeTemp = nodeTemp + 1
            print('')
        for i in range(self.nodes - nodeTemp):
            print(f'{self.listHeapMaximum[nodeTemp]}', end=' ')
            nodeTemp = nodeTemp + 1
        print('')

    def size(self):
        return self.nodes