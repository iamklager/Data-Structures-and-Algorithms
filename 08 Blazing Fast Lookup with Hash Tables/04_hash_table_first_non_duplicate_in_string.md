# Chapter 08

## Exercise 04

Write a function that returns the first non-duplicated character in a string. For example, the string, "minimum" has two characters that only exist once-the "n" and the "u", so your fucntion should return the "n", since it occurs first. The function should have an efficiency of $O(N)$.

```python
def f_FirstNonDup(string):
    hash_table = {}
    
    for c in string:
        if hash_table.get(c) != None:
            hash_table[c] += 1
        else:
            hash_table[c] = 1
    for key in hash_table:
        if hash_table.get(key) == 1:
            return key
    
    return None


s = "minimum"

print(f_FirstNonDup(s))
```

