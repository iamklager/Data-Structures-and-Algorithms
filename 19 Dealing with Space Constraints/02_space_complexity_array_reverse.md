# Chapter 19

## Exercise 02

Following is a function that reverses an array. Describe its space complexity in terms of Big O:

```js
function reverse(array) {
  let newArray = [];

  for (let i = array.length - 1; i >= 0; i--) {
    newArray.push(array[i]);
  }
  return newArray;
}
```

$O\left( N \right)$

