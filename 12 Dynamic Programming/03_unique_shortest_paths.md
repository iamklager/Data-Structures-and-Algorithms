# Chapter 12

## Exercise 03

Here is a solution to the "Unique Paths" problem from an exercise int he previous chapter. Use memoization to improve its efficiency:

```ruby
def unique_paths(rows, columns)
  return 1 if rows == 1 || columns == 1
  return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
end
```

```ruby
def unique_paths(rows, columns, h = {})
  return 1 if rows == 1 || columns == 1
  if !h[[rows, columns]]
    h[[rows, columns]] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, h)
  end
  
  return h[[rows, columns]]
end
```
