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