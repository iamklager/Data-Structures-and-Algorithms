# Chapter 08

## Exercise 03

Write a function that accepts a string that contains all the letters of the alphabet expect one and returns the missing letter. For example, the string "the quick brown box jumps over a lazy dog" contains all the letters of the alphabet except the letter, "f". The function should have a time complexity of $O(N)$.

```python
def f_MissingLetter(string):
    hash_table = {}
    for c in string:
        if c != ' ':
            hash_table[c] = True
    for l in "abcdefghijklmnopqrstuvwxyz":
        if hash_table.get(l) == None:
            return l
    
    return None


s = "the quick brown box jumps over a lazy dog"

print(f_MissingLetter(s))
```

