
# Chapter 03

## Exercise 03

The following function is based on the age-old analogy used to describe the power of compounding interest:

...

Use Big O Notation to describe the time complexity of this function, which is below:

```js
function chessboardSpace(numberOfGrains) {
  let chessboardSpaces = 1;
  let placedGrains = 1;
  
  while (placedGrains < numberOfGrains) {
    placedGrains *= 2;
    chessboardSpaces += 1;
  }
  
  return chessboardSpaces;
}
```

$O(log\text{ }N)$
