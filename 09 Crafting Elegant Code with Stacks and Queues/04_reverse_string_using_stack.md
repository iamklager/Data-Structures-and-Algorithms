# Chapter 09

## Exercise 04

Write a function that uses a stack to reverse a string. (For example, "abcde" would become "edcba".) You can work with our earlier implementation of the Stack class.  

```python
def f_ReverseString(string):
    stack = []
    res = ""
    
    for c in string:
        stack.append(c)
    
    while stack:
        res += stack.pop()
    
    return res


s = "abcde"
print(f_ReverseString(s))
```

