# A node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


# A doubly linked list class
class DoublyLinkedList:
    def __init__(self, first_node = None, last_node = None):
        self.first_node = first_node
        self.last_node  = last_node
    
    def insert_at_end(self, value):
        new_node = Node(value)
        
        if self.first_node is None:
            self.first_node = new_node
            self.last_node  = new_node
        else:
            new_node.prev_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node
    
    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        
        return removed_node
    
    def print_all_rev(self):
        if self.last_node is None:
            return None
        current_node = self.last_node
        while 1:
            print(current_node.data)
            if current_node.prev_node is None:
                break
            current_node = current_node.prev_node


# A queue class
class Queue:
    def __init__(self):
        self.data = DoublyLinkedList()
    
    def enqueue(self, element):
        removed_node = self.data.remove_from_front()
        
        return removed_node.data
    
    def read(self):
        if self.data.first_node is None:
            return None
        else:
            return self.data.first_node