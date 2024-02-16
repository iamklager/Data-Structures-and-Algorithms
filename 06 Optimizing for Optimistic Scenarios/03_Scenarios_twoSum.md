# Chapter 06

## Exercise 03

The following function checks whether an array of numbers contains a pair of two numbers that add up to 10.

```js
function twoSum(array) {
  for (let i = 0; i < array.length; i++ {
    for (let j = 0; j < array.length; j++) {
      if (i !== j && array[i] + array[j] === 10) {
        return true;
      }
    }
  }
  return false;
}
```

What are the best-, average-, and worst-case scenarios? Then, express the worst-case scenario in terms of Big O Notation.

**Best Case:** The first two numbers sum up to $10$.  
**Average Case:** The middle two numbers sum up to $10$.  
**Worst Case:** No numbers sum up to $10$ $\left(\text{i.e. }O\left(N^2\right)\right)$
