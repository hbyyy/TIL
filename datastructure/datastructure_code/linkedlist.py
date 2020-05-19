class Node:
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newData):
        self.value = newData

    def setNext(self, newpointer):
        self.pointer = newpointer


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer

    def _addFirst(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node

    def _deleteFirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print('리스트가 비었습니다')

    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

    def addNode(self, value):
        if not self.head:
            self._addFirst(value)
        else:
            self._add(value)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False

        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
            return node, prev, found

    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print(f'인덱스 {index}에 해당하는 노드가 없습니다')

    def deleteNodeByValue(self, value):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find_by_value(value)
            if node and i == index:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print(f'값 {value}에 해당하는 노드가 없습니다')


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.length = 0

    def _printlist(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer

    def _delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

    def _add(self, value):
        self.length += 1
        self.head = Node(value, self.head)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def deleteNode(self, index):
        node, prev, i = self._find(index)
        if index == i:
            self._delete(prev, node)
        else:
            print(f'인덱스 {index} 노드가 없습니다')

    def deleteNodeByValue(self, value):
        node, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev, node)
        else:
            print(f'값 {value} 노드가 없습니다')