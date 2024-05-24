# Chapter 14

## Exercise 05

Here's a brilliant little linked list puzzle for you. Let's say you have access to a node from somewhere in the middle of a classic linked list, but not the linked list itself. That is, you have a variable that points to an instance of Node, but you don't have access to the LinkedList instance. In this situation, if you follow this node's link, you can find all the items form this middle node until the end, but you have no way to find the nodes that precede this node in the list.<br>
<br>
Write code that will effectively delete this node from the list. The entire remaining list should remain complete, with only this node removed.

```python
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


# Testing
node_1 = Node(data = "once")
node_2 = Node(data = "upon")
node_3 = Node(data = "a")
node_4 = Node(data = "time")
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4
lst = LinkedList(first_node = node_1)

lst.print_all()
print("")
lst.delete_middle_node(node_3)
lst.print_all()
```
