# Chapter 15

## Exercise 05

There is yet another form of traversal called postorder traversal. Here is the code as applied to our book app:
```python
def traverse_and_print(node):
    if node is None:
        return
    traverse_and_print(node.leftChild)
    traverse_and_print(node.rightChild)
    print(node.value)
```
For the example tree in the text (which also appears in the previous exercise), write out the order in which the book titles are printed with postorder traversal.

1. "Alice in Wonderland"
2. "Lord of the Flies"
3. "Great Expectations"
4. "Pride and Prejudice"
5. "The Odyssey"
6. "Robinson Crusoe"
7. "Moby Dick"