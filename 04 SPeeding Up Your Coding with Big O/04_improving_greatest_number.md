
# Chapter 04

## Exercise 04

The following function finds the greatest single number within an array, but has an efficiency of $O\left(N^2\right)$. Rewrite the function so that it becomes a speey $O(N)$:

```python
def greatestNumber(array):
    for i in array:
        # Assume for now that i is the greatest:
        isIValTheGreatest = True
        
        for j in array:
            # If we find another value that is greater than i,
            # i is not the greatest:
            if j > i:
                isIValTheGreatest = False
            
        # If, by the time we checked all other numbers, i
        # is still the greatest, it means that i is the greatest number:
        if isIValTheGreatest:
            return i
```

```python
def greatestNumber2 (array):
    greatestNumberSoFar = array[0]
    for number in array[1:]:
        if number > greatestNumberSoFar:
            greatestNumberSoFar = number
    return greatestNumber
```


