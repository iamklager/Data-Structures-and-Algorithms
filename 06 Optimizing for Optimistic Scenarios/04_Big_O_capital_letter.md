# Chapter 06

## Exercise 04

The following function returns whether or not a capital "X" is present within a string.

```js
function containsX(string) {
  foundX = false;
  
  for (let i = 0; i < string.length; i++) {
    if (string[i] === "X") {
      foundX = true;
    }
  }
  
  return foundX
  
}
```

What is this fucntion's time complexity in terms of Big O Notation?

$O(N)$

Then, modify the code to improve the algorithm's efficiency for best- and average-case scenarios.

```js
function containsX(string) {
  for (let i = 0; i < string.length; i++) {
    if (string[i] === "X") {
      return true;
    }
  }
  
  return false;
}
```

