# Chapter 15

## Exercise 05

In the text I demonstrated how to use inorder traversal to print a list of all the book titles. Another way to traverse a tree is known as preorder traversal. Here is the code for it as applied to our book app:
```python
def traverse_and_print(node):
    if node is None:
        return
    print(node.value)
    traverse_and_print(node.leftChild)
    traverse_and_print(node.rightChild)
```
For the example tree in the text (the one with Moby Dick and the other book titles), write out the order in which the book titles are printed with preorder traversal.

1. "Moby Dick"
2. "Great Expectations"
3. "Alice in Wonderland"
4. "Lord of the Flies"
5. "Robinson Crusoe"
6. "Pride and Prejudice"
7. "The Odyssey"