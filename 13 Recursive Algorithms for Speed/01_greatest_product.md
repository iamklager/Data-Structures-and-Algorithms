# Chapter 13

## Exercise 01

Given an array of positive numbers, write a function that returns the greatest product of any three numbers. The approach of using three nested loops would clock in at $O\left(N^3\right)$, which is very slow. Use sorting to implement the function in a way that it computes at $O\left(\log N\right)$ speed. (There are even faster implementations, but we're focusing on using sorting as a technique to make code faster).

```python
def GreatestProduct(array):
    n = len(array) - 1
    array.sort() # alternatively use quick sort but I am lazy
    
    return array[n] * array[n-1] * array[n-2]


a = [6, 3, 8, 2, 4, 9, 5]
print(GreatestProduct(a))

```

