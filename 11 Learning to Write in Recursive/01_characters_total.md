# Chapter 11

## Exercise 01

Use recursion to write a function that accepts an array of strings and returns the total number of characters across all the strings. For example, if the input array is ["ab", "c", "def", "ghij"], the output should be $10$ since there are $10$ characters in total.

```python
def characters_total(array):
    if len(array) == 0:
        return 0
    else:
        return len(array[0]) + characters_total(array[1:])


a = ["ab", "c", "def", "ghij"]
print(characters_total(a))
```

