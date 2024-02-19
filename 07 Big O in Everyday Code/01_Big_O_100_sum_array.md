# Chapter 07

## Exercise 01

Use Big O Notation to describe the time complexity of the following function. The function returns true if the array is a "100-Sum Array," and false if not.  
  
A "100-Sum Array" meets the following criteria:

- Its first and last numbers add up to 100.
- Its second and second-to-last numbers add up to 100.
- Its third and third-to-last numbers add up to 100, and so on.

Here is the function:
```python
def one_hundred_sum?(array)
    left_index = 0
    right_index = array.length - 1
    
    while left_index < array.length / 2
        if array[left_index] + array[right_index] != 100
            return false
        end
        
        left_index += 1
        right_index -= 1
    end
    
    return true
end
```

$O(N)$
