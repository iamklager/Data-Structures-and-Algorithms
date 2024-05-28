# Chapter 20

## Exercise 05

You are to write a function that sorts these readings from lowest to highest.  

If you used a classic sorting algorithm such as Quicksort, this would take $O(N \log(N))$. However, in this case, it's actually possible to write a faster sorting algorithm.

```python
def ONSort(array):
    d = {}

    for a in array:
        if a in d:
            d[a] += 1
        else:
            d[a]  = 1
    
    res = []
    for temp in range(970, 991):
        if temp / 10 in d:
            for i in range(d[temp / 10]):
                res.append(temp / 10)
    return res


a = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
print(ONSort(a))
```