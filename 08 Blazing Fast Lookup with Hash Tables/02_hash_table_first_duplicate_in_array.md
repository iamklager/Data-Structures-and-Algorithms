# Chapter 08

## Exercise 02

Write a function that accepts an array of strings and returns the first duplicate value it finds. For example, if the array is ["a", "b", "c", "d", "c", "e", "f"], the function should return "c", since its duplicated within the array. (You can assume that there's one pair of duplicates within the array.) Make sure the function has an efficiency of $O(N)$.

```python
def f_FirstDupInArray(array):
    hash_table = {}
    
    for e in array:
        if hash_table.get(e):
            return e
        hash_table[e] = True
    
    return None


a = ["a", "b", "c", "d", "c", "e", "f"]

print(f_FirstDupInArray(a))
```
