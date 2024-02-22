# Chapter 12

## Exercise 01

The following function accepts an array of numbers and returns the sum, as long as a particular number doesn't bring the sum above 100. If adding a particular number will make the sum higher than 100, that number is ignored. However, this function makes unnecessary recursive calls. Fix the code to eliminate the unnecessary recursion:

```ruby
def add_until_100(array)
  return 0 if array.length == 0
  if array[0] + add_until_100(array[1, array.length - 1]) > 100
    return add_until_100(array[1, array.length - 1])
  else
    return array[0] + add_until_100(array[1, arra.length -1])
  end
end
```

```ruby
def add_until_100(array)
  return 0 if array.length == 0
  res = 0
  array.each do |a|
    if res + a > 100
      break
    else
      res = res + a
    end
  end
  return res
end
```
