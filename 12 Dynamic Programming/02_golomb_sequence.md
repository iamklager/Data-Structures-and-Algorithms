# Chapter 12

## Exercise 02

The following function uses recursion to calculate the Nth number from a mathematical sequence known as the "Golomb sequence." It's terribly inefficient, though! Use memoization to optimize it.

```ruby
def golomb(n)
  return 1 if n == 1
  return 1 + golomb(n - golomb(golomb(n - 1)));
end
```

```ruby
def golomb(n, h = {})
  return 1 if n == 1
  
  if !h[n]
    h[n] = 1 + golomb(n - golomb(golomb(n - 1, h), h), h)
  end
  
  return h[n]
end
```
