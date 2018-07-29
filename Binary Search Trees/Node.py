
class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data < self.data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def getMin(self):
        if not self.left:
            return self.data
        else:
            return self.left.getMin()

    def getMax(self):
        if not self.right:
            return self.data
        else:
            return self.right.getMax()

    def traverseInOrder(self):
        if self.left is not None:
            self.left.traverseInOrder()
        print(self.data)
        if self.right is not None:
            self.right.traverseInOrder()

    def remove(self, data, parentNode):
        if data < self.data:
            if self.left is not None:
                self.left.remove(data, self)
        elif data < self.data:
            if self.right is not None:
                self.right.remove(data, self)
        else:
            if self.left is not None and self.right is not None:
                self.data = self.right.getMin()
                self.right.remove(self.data, self)
            elif parentNode.left == self:
                if self.left is not None:
                    tempNode = self.left
                else:
                    tempNode = self.right
                parentNode = self.right
            elif parentNode.right == self:
                if self.left is not None:
                    tempNode = self.left
                else:
                    tempNode = self.right
                parentNode.right = tempNode
