from Node import Node

class LinkedList(object):
    """Linked Lists implementation in python"""
    def __init__(self):
        """Initalizes the head as None and sets the counter to 0"""
        self.head = None
        self.counter = 0

    def insertStart(self, data):
        """Inserts the data as a node in O(1) time."""
        self.counter += 1
        newNode = Node(data)
        if self.head == None:
            self.head = newNode 
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size(self):
        """Returns the size of the list in O(1) time."""
        #Could have computed the size here but that would result in O(n) time complexity
        #Whereas using the counter gives O(1) time complexity
        return self.counter

    def insertEnd(self, data):
        """Inserts an element in the end of the linked list in O(n) time."""
        self.counter += 1 #Increment the counter
        if self.head == None:
            #If there is no head, set the data as the head
            self.insertStart(data)
        else:
            newNode = Node(data)
            actualNode = self.head
            while actualNode.nextNode is not None:
                actualNode = actualNode.nextNode
            actualNode.nextNode = newNode

    def remove(self, data):
        """Removes the data from the linked list in O(n) time."""
        if self.counter == 0:
            raise IndexError  #If the list is empty, return
        else:
            self.counter -= 1   #Else decrement the counter
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)

    def traverseList(self):
        """Prints all the elements in the linked list in O(n) time."""
        #While there are next nodes to the current node, 
        #keep printing the data in the nodes
        actualNode = self.head
        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

    def insertIndex(self, index, data):
        """Inserts data at index i in O(n) time."""
        #Get the node before index i, set its next node to data 
        #and set the data's next node to node after index i
        actualNode = self.head
        try:
            for i in range(index - 1):
                actualNode = actualNode.nextNode
        except:
            raise IndexError
        self.counter += 1 #Increment the counter
        newNode = Node(data)
        newNode.nextNode = actualNode.nextNode
        actualNode.nextNode = newNode

    def index(self, index):
        """Returns the data at given index"""
        #Get the node at index index and return its data
        #If actualNode becomes None then actualNode.nextNode 
        #raises atrribute error which is caught and an 
        #index error is raised instead
        actualNode = self.head
        try:
            for i in range(index):
                actualNode = actualNode.nextNode
        except:
            raise IndexError
        return actualNode.data

    def search(self, data):
        """Returns the index of the first occurence of data in the linked list. Returns None if element not in list"""
        #Check if head is none. If not then check that data = self.head and return 0.
        #Else keep moving on to next nodes and incrementing the index counter
        #return index if element is found else return None
        currentNode = self.head
        index = 0
        if currentNode == None:
            return None

        if data == currentNode.data:
            return index 
        else:
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
                index += 1
                if data == currentNode.data:
                    return index
            return None

