class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtBegin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insertNodeAtEnd(self, value):
        pass

    def updateNode(self, value, index):
        pass

    def removeFirstNode(self):
        pass

    def removeAtIndex(self, index):
        pass

    def removeNode(self, data):
        pass

    def printLinkedList(self):
        pass


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtBegin(self, value):
        pass

    def insertNodeAtEnd(self, value):
        pass

    def updateNode(self, value, index):
        pass

    def removeFirstNode(self):
        pass

    def removeAtIndex(self, index):
        pass

    def removeNode(self, data):
        pass

    def printLinkedList(self):
        pass


if __name__ == '__main__':
    linked_list = LinkedList()

    # Add nodes to the linked list
    linked_list.insertNodeAtEnd(1)
