# Chapter 08

## Exercise 01

Write a function that returns the intersection of two arrays. The intersection is a third array that contains all values contained within the first two arrays. For example, the intersection of [1,2,3,4,5] and [0,2,4,6,8] is [2,4]. Your function should have a complexity of $O(N)$. (If your programming language has a built-in way of doing this, don't use it. The idea is to build the algorithm yourself.)

```python
def f_Intersect(array_1, array_2):
    hash_table = {}
    intersect = []
    
    for e in array_1:
        hash_table[e] = True
    for e in array_2:
        if hash_table.get(e):
            intersect.append(e)
    
    return intersect


a_1 = [1,2,3,4,5]
a_2 = [0,2,4,6,8]

print(f_Intersect(a_1, a_2))
```
