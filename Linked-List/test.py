from random import randrange
from LinkedList import LinkedList

linkedList = LinkedList()

for i in range(10):
    linkedList.insertEnd(randrange(0, 10))
linkedList.insertStart(123)
print("t1")
linkedList.traverseList()
print("size:", linkedList.size())
 
linkedList.remove(123)

print("t2")
linkedList.traverseList()
print("size:", linkedList.size())

linkedList.insertIndex(2, 100)

print("t3")
linkedList.traverseList()
print("size:", linkedList.size())

print("element 3: ", linkedList.index(2))