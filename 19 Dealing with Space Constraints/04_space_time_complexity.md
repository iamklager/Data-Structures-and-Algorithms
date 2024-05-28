# Chapter 19

## Exercise 04

Following are three different implementations of a function that accepts an array of numbers and returns an array containing those numbers multiplied by 2. For example, if the input is [5, 4, 3, 2, 1], the output will be [10, 8, 6, 4, 2].

```js
function doubleArray1(array) {
  let newArray = [];

  for(let i = 0; i < array.length; i++) {
    newArray.push(array[i] * 2);
  }
  return newArray;
}
function doubleArray2(array) {
  for(let i = 0; i < array.length; i++) {
    array[i] *= 2;
  }
  return array;
}
function doubleArray3(array) {
  if (index >= array.length) { return; }

  array[index] *= 2;
  doubleArray3(array, index + 1);
  
  return array;
}
```

Fill in the table that follows to describe the efficiency of these three versions in the terms of both time and space:

| **Version** | **Time Complexity** | **Space Complexity** |
|-------------|---------------------|----------------------|
| Version #1  |          ?          |           ?          |
| Version #2  |          ?          |           ?          |
| Version #3  |          ?          |           ?          |


| **Version** | **Time Complexity** | **Space Complexity** |
|-------------|---------------------|----------------------|
| Version #1  |        $O(N)$       |        $O(N)$        |
| Version #2  |        $O(N)$       |        $O(1)$        |
| Version #3  |        $O(N)$       |        $O(N)$        |

