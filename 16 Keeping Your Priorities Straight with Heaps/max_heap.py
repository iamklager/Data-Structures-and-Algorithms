class MaxHeap:
    def __init__(self):
        self.data = []
    
    def root_node(self):
        return self.data[0]
    
    def last_node(self):
        return self.data[-1]
    
    def left_child_index(self, index):
        return index * 2 + 1
    
    def right_child_index(self, index):
        return index * 2 + 2

    def parent_index(self, index):
        return (index - 1) // 2
    
    def insert(self, value):
        self.data.append(value)
        new_node_index = len(self.data) - 1
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parent_index(new_node_index)]
            new_node_index = self.parent_index(new_node_index)
    
    def has_greater_child(self, index):
        (
            self.data[self.left_child_index(index)] and self.data[self.left_child_index(index)] > self.data[index]
        ) or (
            self.data[self.right_child_index(index)] and self.data[self.right_child_index(index)] > self.data[index]
        )

    def calculate_larger_child_index(self, index):
        if not self.data[self.right_child_index(index)]:
            return self.left_child_index(index)
        if self.data[self.right_child_index(index)] > self.data[self.left_child_index(index)]:
            return self.right_child_index(index)
        else:
            return self.left_child_index(index)
    
    def delete(self):
        del_val = self.root_node
        self.data[0] = self.data.pop()
        trickle_node_index = 0
        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            self.data[trickle_node_index], self.data[larger_child_index] = self.data[larger_child_index], self.data[trickle_node_index]
            trickle_node_index = larger_child_index
        return del_val

