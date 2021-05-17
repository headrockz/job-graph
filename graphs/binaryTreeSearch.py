class Node:

    def __init__(self, value):
        self.value = value
        self.childrenLeft = None
        self.childrenRight = None

    def getValue(self):
        return self.value

    def setChildrenLeft(self, value):
        self.childrenLeft = value

    def setChildrenRight(self, value):
        self.childrenRight = value

    def getChildrenLeft(self):
        return self.childrenLeft

    def getChildrenRight(self):
        return self.childrenRight

class BinaryTreeSearch:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, value):
        print('Entrou no insert')
        no = Node(value)
        if self.root is None:
            self.root = no
        else:
            nodeFather = None
            nodeCurrent = self.root
            while True:
                if nodeCurrent is not None:
                    nodeFather = nodeCurrent
                    if no.getValue() < nodeCurrent.getValue():
                        nodeCurrent = nodeCurrent.getChildrenLeft()
                    else:
                        nodeCurrent = nodeCurrent.getChildrenRight()
                else:
                    if no.getValue() < nodeFather.getValue():
                        nodeFather.setChildrenLeft()
                    else:
                        nodeFather.setChildrenRight(no)
                        break

    def previewTree(self, nodeCurrent): # Percurso em ordem simétrica
        if nodeCurrent is not None:
            self.previewTree(nodeCurrent.getChildrenLeft())
            print(f'{nodeCurrent.getValue()}', end=' ')
            self.previewTree(nodeCurrent.getChildrenRight())


t = BinaryTreeSearch()

t.insert(8)
t.insert(10)

t.previewTree(t.getRoot())
