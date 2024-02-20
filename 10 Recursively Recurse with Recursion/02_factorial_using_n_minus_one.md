# Chapter 10

## Exercise 02

My kid was playing with my computer and changed my factorial function so that it computes factorial based on $(n-2)$ instead of $(n-1)$. Predict what will happen when we run factorial(10) using this function:

```ruby
def factorial(n)
  return 1 if n == 1
  return n * factorial(n - 2)
end
```

factorial(10) would end up running infinitely (or until we reach stack overflow), since we never reach factorial(1), but instead factorial(0), factorial(-2), and so on.
