
# Chapter 04

## Exercise 03

Use Big O Notation to describe the time complexity of the following function. It finds the greatest product of any pair of two numbers within a given array:

```python
def greatestProduct(array):
  greatestProductSoFar = array[0] * array[1]
  
  for i, iVal in enumerate(array):
    for j, jVal in enumerate(array):
      if i != j and iVal * jVal > greatestProductSoFar:
        greatestProductSofFar = iVal * jVal
  
  return greatestProductSoFar
```

$O\left(N^2\right)$
