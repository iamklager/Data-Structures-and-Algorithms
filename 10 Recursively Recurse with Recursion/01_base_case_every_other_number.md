# Chapter 10

## Exercise 01

The following function prints every other number from a low number to a high number. For example, if low is $0$ and high is $10$, it would print:  

$0$  
$2$  
$4$  
$6$  
$8$  
$10$ 

Identify the base case in the function:

```ruby
def print_every_other(low, high)
  return if low > high
  puts low
  print_every_other(low + 2, high)
end
```

Base case:
```ruby
low > high
```
