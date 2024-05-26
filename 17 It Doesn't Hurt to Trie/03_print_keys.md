# Chapter 17

## Exercise 03

Write a function that traverses each node of a trie and prints each key, including all "*" keys.

```python
def print_keys(self, node):
    current_node = node or self.root
    for key, child_node in current_node.children.items():
        print(key)
        if key != "*":
            self.print_keys(child_node)
```