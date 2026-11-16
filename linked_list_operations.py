class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, key):
        new_node = Node(key)
        # Link the new node to the old head before moving the head.
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def pop_front(self):
        if self.head is None:
            raise IndexError("List is empty")

        value = self.head.key
        self.head = self.head.next

        # Removing the last node also clears the tail.
        if self.head is None:
            self.tail = None

        return value

    def push_back(self, key):
        new_node = Node(key)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_back(self):
        if self.head is None:
            raise IndexError("List is empty")

        if self.head is self.tail:
            value = self.tail.key
            self.head = None
            self.tail = None
            return value

        current = self.head

        # Find the node before the tail so it can become the new tail.
        while current.next is not self.tail:
            current = current.next

        value = self.tail.key
        current.next = None
        self.tail = current

        return value

    def top_front(self):
        if self.head is None:
            raise IndexError("List is empty")
        return self.head.key

    def top_back(self):
        if self.tail is None:
            raise IndexError("List is empty")
        return self.tail.key

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current

            current = current.next

        return None

    def add_after(self, node, key):
        if node is None:
            raise ValueError("Node cannot be None")

        new_node = Node(key)
        # Preserve the rest of the chain before inserting the new node.
        new_node.next = node.next
        node.next = new_node

        if self.tail is node:
            self.tail = new_node

    def is_empty(self):
        return self.head is None

    def display(self):
        current = self.head

        while current is not None:
            print(current.key, end=" -> ")
            current = current.next

        print("None")


# Test the linked list
lst = LinkedList()

lst.push_back(7)
lst.push_back(10)
lst.push_back(4)
lst.push_back(13)

lst.display()

lst.push_front(26)
lst.display()

lst.pop_front()
lst.display()

lst.push_back(8)
lst.display()

lst.pop_back()
lst.display()

node = lst.find(10)
lst.add_after(node, 99)
lst.display()
