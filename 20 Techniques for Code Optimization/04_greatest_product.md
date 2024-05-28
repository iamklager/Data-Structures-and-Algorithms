# Chapter 20

## Exercise 04

You're writing a function that accepts an array of numbers and computes the highest product of any two nubmers in the array. At first glance, this is the highest product of any two numbers in the array. At first glance, this is easy, as we can just find the two greatest numbers and multiply them. Hwever, our array con contain negative numbers and look like this:  

[5, -10, -6, 9, 4]  

In this case, it's actually the product of the two lowest numbers, -10 and -6 that yield the highest product of 60.  

We could use nested loops to multiply every possible pair of numbers, but this would take $O\left(N^2 \right)$ time. Your job is to optimize the function so that it's a speedy $O(N)$.

```python
def GreatestProduct(array):
    greatest_numb        = float("-inf")
    second_greatest_numb = float("-inf")
    lowest_numb          = float("inf")
    second_lowest_numb   = float("inf")
    
    for a in array:
        if a >= greatest_numb:
            second_greatest_numb = greatest_numb
            greatest_numb = a
        elif a < lowest_numb:
            second_lowest_numb   = lowest_numb
            lowest_numb   = a
    
    prod_pos = greatest_numb * second_greatest_numb
    prod_neg = lowest_numb   * second_lowest_numb
    
    if prod_pos > prod_neg:
        return prod_pos
    elif prod_pos < prod_neg:
        return prod_neg


a = [5, -10, -6, 9, 4]
print(GreatestProduct(a))
```