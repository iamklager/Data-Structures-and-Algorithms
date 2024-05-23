# Chapter 13

## Exercise 03

Write three different implementations of a function that finds the greatest number within an array. Write one function that is $O\left(N^2\right)$, one that is $O(N\log N)$, and one that is $O(N)$.

```python
# O(N^2)
def SortArray1(array):
    greatest_number = array[0]
    
    for i in range(0, len(array)):
        greatest_number = True
        
        for j in range(0, len(array)):
            if array[j] > array[i]:
                greatest_number = False
        
        if greatest_number:
            return array[i]

# O(N log N)
def SortArray2(array):
    array.sort()
    
    return array[-1]

# O(N)
def SortArray3(array):
    greatest_number = array[0]
    
    for i in range(1, len(array)):
        if array[i] > greatest_number:
            greatest_number = array[i]
    
    return greatest_number


a = [9, 3, 2, 5, 6, 7, 1, 0, 4]

print(SortArray1(a))
print(SortArray2(a))
print(SortArray3(a))

```