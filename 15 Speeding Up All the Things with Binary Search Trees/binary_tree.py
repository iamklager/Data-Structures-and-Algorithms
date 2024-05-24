class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left_child = left
        self.right_child = right

def search(value, node):
    if node is None or node.value == value:
        return node
    elif value < node.value:
        search(value, node.left_child)
    else:
        search(value, node.right_child)

def insert(value, node):
    if value < node.value:
        if node.left_child is None:
            node.left_child = TreeNode(value)
        else:
            insert(value, node.left_child)
    elif value > node.value:
        if node.right_child is None:
            node.right_child = TreeNode(value)
        else:
            insert(value, node.right_child)

def lift(node, del_node):
    if node.left_child is not None:
        node.left_child = lift(node.left_child, del_node)
        return node
    else:
        del_node.value = node.value
        return node.right_child

def delete(value, node):
    if node is None:
        return None
    elif value < node.value:
        node.left_child = delete(value, node.left_child)
        return node
    elif value > node.value:
        node.right_child = delete(value, node.right_child)
        return node
    elif value == node.value:
        if node.left_child is None:
            return node.right_child
        elif node.right_child is None:
            return node.left_child
        else:
            node.right_child = lift(node.right_child, node)
            return node

def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left_child)
    print(node.value)
    inorder_traversal(node.right_child)

def greatest_value(node):
    if node.right_child is None:
        return node.value
    return greatest_value(node.right_child)

def preorder_traversal(node):
    if node is None:
        return
    print(node.value)
    preorder_traversal(node.left_child)
    preorder_traversal(node.right_child)

def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left_child)
    postorder_traversal(node.right_child)
    print(node.value)


node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
