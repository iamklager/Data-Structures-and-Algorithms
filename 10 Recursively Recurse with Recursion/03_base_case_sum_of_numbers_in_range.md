# Chapter 10

## Exercise 03

Following is a function in which we pass in two numbers called low and high. The function returns the sum of all the numbers from low to high. For example, if low is $1$, and high is $10$, the function will return the sum of all numbers from $1$ to $10$, which is $55$. However, our code is missing the base case, and will run indefinitely! Fix the cody by adding the correct base case:

```ruby
def sum(low, high)
  return high + sum(low, high - 1)
end
```

Fixed:
```ruby
def sum(low, high)
  if low == high
    return low
  return high + sum(low, high - 1)
end
```
