# Chapter 19

## Exercise 01

Following is the "Word Builder" algorithm we encountered in Word Builder, on page 97. Describe its space complexity in terms of Big O:

```js
function wordBuilder(array) {
  let collection = [],

  for(let i = 0; i< array.length; i++) {
    for(let j = 0; j < array.length; j++) {
      if (i !== j) {
        collection.push(array[i] + array[j]);
      }
    }
  }
  return collection
}
```

$O\left( N^2 \right)$

