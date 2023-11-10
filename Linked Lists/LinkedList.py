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

    def deleteNode(self, index):
        current_node = self.head
        current_index = 0

        # Delete the head node
        if current_index == index:
            self.head = current_node.next
            return

        previous_node = self.head
        while current_node.next:
            if current_index == index:
                previous_node.next = current_node.next
                return
            previous_node = current_node
            current_index += 1
            current_node = current_node.next

    def searchForNode(self, data):
        current_node = self.head
        current_index = 0

        while current_node.next:
            if current_node.data == data:
                return current_index
            current_index += 1
            current_node = current_node.next
        # Node not found
        return None

    def reverseLinkedList(self):
        previous_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

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

    # Delete node at index 0
    linked_list.deleteNode(0)

    linked_list.printLinkedList()
    print()

    # Delete node at index 4
    linked_list.deleteNode(4)

    linked_list.printLinkedList()
    print()

    # Search for 7 in the linked list
    print(linked_list.searchForNode(7))

    # Search for 4 in the linked list
    print(linked_list.searchForNode(4))
    print()

    # Reverse Linked list
    linked_list.reverseLinkedList()

    linked_list.printLinkedList()
    print()
