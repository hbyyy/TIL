from linkedlist import LinkedListQueue

ll = LinkedListQueue()
for i in range(1, 5):
    ll.addNode(i)
ll._printList()
ll.deleteNode(2)
ll.addNode(15)