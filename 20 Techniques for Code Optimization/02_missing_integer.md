# Chapter 20

## Exercise 02

You're writing a function that accepts an array of distinct integers from 0, 1, 2, 3...up to N. However, the array will be missing one integer, and your function is to return the missing one.  

Using a nested-loops approach would take up $O\left(N^2 \right)$. Your job is to optimize the code so that it has a runtime of $O(N)$.

```python
a = [2, 3, 0, 6, 1, 5]

def MissingInt(array):
    sum = 0
    n = len(array)
    for e in array:
        sum += e
    gauss_sum = (n * (n + 1)) / 2

    return gauss_sum - sum

print(MissingInt(a))
```