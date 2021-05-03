class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def getValueNode(self):
        return self.value

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

nodeOne = Node(1)
nodeTwo = Node(7)

print(nodeOne.getValueNode())
print(nodeTwo.getValueNode())
nodeOne.setNext(nodeTwo)
print(nodeOne.getNext())
print(nodeOne.getNext().getValueNode())