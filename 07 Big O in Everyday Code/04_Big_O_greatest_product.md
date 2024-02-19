# Chapter 07

## Exercise 04

Use Big O Notation to describe the time complexity of the following function. This function finds the greatest product of three numbers from a given array:

```ruby
def largest_product(array)
  largest_product_so_far = array[0] * array[1] * array[2]
  i = 0
  
  while i < array.length
    j = i + 1
    while j < array.length
      k = j + 1
      while k < array.length
        if array[i] * array[j] * array[k] > largest_product_so_far
          largest_product_so_far = array[i] * array[j] * array[k]
        end
        k += 1
      end
      j += 1
    end
    i += 1
  end
  
  return largest_product_so_far

end
```

$O(N^3)$
