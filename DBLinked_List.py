class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DBLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
    def delete(self, data):
        node = self.head
        if node.data == data:
            self.head = node.next
            del node
        else:
            while node.next:
                next_node = node.next
                if next_node.data == data:
                    node.next = next_node.next
                    del next_node
                else:
                    node = node.next
    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next