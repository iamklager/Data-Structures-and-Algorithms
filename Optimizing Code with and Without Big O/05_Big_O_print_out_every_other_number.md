
# Chapter 05

## Exercise 05

The next function iterates over an array of numbers. As it does so, it focuses on every other number while ignoring the numbers in between. For each "focus number", the function proceeds to print out every number from the array - one at a time - after being added to the focus number.

What is this function's efficiency in terms of Big O Notation?

```ruby
def every_other(array)
  array.each_with_index do |number, index|
    if index.even?
      array.each do |other_number|
        puts number + other_number
      end
    end
  end
end
```

$O\left(N^2\right)$
