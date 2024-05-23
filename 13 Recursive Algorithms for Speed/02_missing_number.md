# Chapter 13

## Exercise 02

The following function finds the "missing number" from an array of integers. That is, the array is expected to have all integers from $0$ up to the array's length, but one is missing. As examples, the array, [5, 2, 4, 1, 0] is missing the number $3$, and the array [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the number $8$.

```js
function findMissingNumber(array) {
  for(let i = 0; i < array.length; i++) {
    if(!array.includes(i)) {
      return i;
    }
  }

  //I If all numbers are present:
  return null;
}
```
Use sorting to write a new implementation of thjis function that only takes $O(N\log N)$. (There are even faster implementations, but we're focusing on using sorting as a technique to make code faster.

```js
function findMissingNumber(array) {
  array.sort((a, b) => (a < b) ? -1 : 1);

  for(let i = 0; i < array.length; i++) {
    if(array[i] !== i) {
      return i;
    }
  }
  return null;
}
```