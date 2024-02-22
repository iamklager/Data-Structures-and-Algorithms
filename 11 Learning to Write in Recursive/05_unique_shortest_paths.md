# Chapter 11

## Exercise 05

This problem is known as the "Unique Paths" problem: Let's say you have a grid of rows and columns. Write a function that accepts a number of rows and a number of columns, and calculates the number of possible "shortest" paths from the upper-leftmost square to the lower-rightmost square.

```python
def unique_shortest_paths(nrow, ncol):
    if (nrow == 1) and (ncol == 1):
        return 1
    elif (nrow > 1) and (ncol == 1):
        return unique_shortest_paths(nrow - 1, ncol)
    elif (nrow == 1) and (ncol > 1):
        return unique_shortest_paths(nrow, ncol - 1)
    else:
        return unique_shortest_paths(nrow - 1, ncol) + unique_shortest_paths(nrow, ncol - 1)


print(unique_shortest_paths(3, 3))
```

