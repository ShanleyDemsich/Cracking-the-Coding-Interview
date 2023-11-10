class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data, index=None):
        new_node = Node(data)

        # If the linked list is empty, set new node as the head
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        current_index = 0

        # Insert new node as the new head of the linked list
        if current_index == index:
            new_node.next = self.head
            self.head = new_node
            return

        # Insert at the given index of the linked list
        while current_node.next:
            if current_index == index:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_index += 1
            current_node = current_node.next

        # Insert at the end of the linked list
        current_node.next = new_node

    def updateNode(self, value, index):
        current_node = self.head
        current_index = 0

        while current_node.next:
            if current_index == index:
                current_node.data = value
                return
            current_index += 1
            current_node = current_node.next

    def deleteNode(self, data, index=None):
        pass

    def findNode(self, data):
        pass

    def reverseLinkedList(self):
        pass

    def printLinkedList(self):
        current_node = self.head
        print(current_node.data)

        while current_node.next:
            current_node = current_node.next
            print(current_node.data)


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
    linked_list.insertNode(1)
    linked_list.insertNode(5)
    linked_list.insertNode(7)
    linked_list.insertNode(2)
    linked_list.insertNode(9)
    linked_list.insertNode(11)
    linked_list.insertNode(0)
    linked_list.insertNode(3)

    # Print the linked list
    linked_list.printLinkedList()
    print()

    # Insert node to the beginning of the Linked List
    linked_list.insertNode(8, 0)

    linked_list.printLinkedList()
    print()

    # Insert node at an index of the linked list
    linked_list.insertNode(6, 3)

    linked_list.printLinkedList()
    print()

    # Update the node at index 3 with the new value 4
    linked_list.updateNode(4, 3)

    linked_list.printLinkedList()
    print()

