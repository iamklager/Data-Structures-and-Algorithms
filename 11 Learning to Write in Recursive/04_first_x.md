# Chapter 11

## Exercise 03

Use recursion to write a function that accepts a string and returns the first index that contains the character "x." For example, the string "abcdefghijklmnopqrstuvwxyz" has an "x" at index 23. To keep things simple, assume the string *definitely* has at least one "x."

```python
def first_x(string, i = 0):
    if string[i] == "x":
        return i
    
    return first_x(string, i + 1)


s = "abcdefghijklmnopqrstuvwxyz"
print(first_x(s))
```

