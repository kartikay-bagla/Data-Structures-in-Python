class Node(object):
    """Node class for Linked List. Each node has its data and a reference to the next node."""
    def __init__(self, data):
        """Initializes the data of the node and sets the nextNode to None"""
        self.data = data
        self.nextNode = None

    def remove(self, data, previous):
        """Removes the data from the linked lists"""
        if self.data == data:
            # If the data to remove is in the current node, 
            # set the previous node's nextNode as the next node 
            # of the current node and delete the current node
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            #Else call this function on the nextNode of current node
            #i.e. go deeper into the linked lists
            if self.nextNode is not None:
                self.nextNode.remove(data, self)