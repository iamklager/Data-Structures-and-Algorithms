
# Chapter 05

## Exercise 03

Use Big O Notation to describe the time complexity of the following function, which returns the sum of all numbers of an array after the numbers have been doubled:

```ruby
def double_then_sum(array)
  doubled_array = []
  
  array.each do |number|
    doubled_array << number * 2
  end
  
  sum = 0
  
  doubled_array.each do |number|
    sum += number
  end
  
  return sum
end

puts double_then_sum([1, 4, 9])
```

$O(N)$
