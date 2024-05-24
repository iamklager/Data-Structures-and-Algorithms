# A node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


# A linked list class
class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node
    
    def read(self, index):
        current_node = self.first_node
        current_index = 0
        
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1
            
            if current_node is None:
                return None
        
        return current_node.data
    
    def index_of(self, value):
        current_node = self.first_node
        current_index = 0
        
        while current_node is not None:
            
            if current_node.data == value:
                return current_index
            
            current_node = current_node.next_node
            current_index += 1
        
        return None
    
    def insert_at_index(self, index, value):
        new_node = Node(value)
        
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return None
        
        current_node = self.first_node
        current_index = 0
        
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1
        
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        
        return None
    
    def delete_at_index(self, index):
        if index == 0:
            self.first_node = self.first_node.next_node
            return None
        
        current_node = self.first_node
        current_index = 0
        
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1
        
        current_node.next_node = current_node.next_node.next_node
        
        return None
    
    def print_all(self):
        if self.first_node is None:
            return None
        
        current_node = self.first_node
        while 1:
            print(current_node.data)
            if current_node.next_node is None:
                break
            current_node = current_node.next_node
    
    def read_last(self):
        if self.first_node is None:
            return None
        current_node = self.first_node
        while current_node.next_node is not None:
            current_node = current_node.next_node
        
        return current_node.data
    
    def reverse(self):
        prev_node = None
        current_node = self.first_node
        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node
        self.first_node = prev_node
    
    def delete_middle_node(self, node):
        node.data = node.next_node.data
        node.next_node = node.next_node.next_node
