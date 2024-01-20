
# Chapter 03

## Exercise 05

The following function calculates the median from an ordered array. Describe its time complexity in terms of Big O Notation:

```js
function median(array) {
  const middle = Math.floor(array.length / 2);
  
  // If array has even amount of numbers:
  if (array.length % 2 === 0) {
    return (array[middle-1] + array[middle]) / 2;
  } else { // If array has odd amount of numbers:
    return array[middle];
  }
}
```

$O(1)$
