# Chapter 11

## Exercise 02

Use recursion to write a function that accepts an array of numbers and returns a new array containing just the even numbers.

```python
def even_numbers(array):
    if len(array) == 0:
        return []
    
    if array[0] % 2 == 0:
        return [array[0]] + even_numbers(array[1:])
    else:
        return even_numbers(array[1:])
        

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(even_numbers(a))
```

