# Chapter 10

## Exercise 04

Here is an array containing both numbers as well as other arrays, which in turn contain numbers and arrays:  
*See array in code cell.*  
Write a recursive function that prints all the numbers (and just numbers).
```python
def f_PrintNumbers(array):
    if not hasattr(array, "__len__"):
        print(array)
    else:
        for e in array:
            f_PrintNumbers(e)


a = [
    1,
    2,
    3,
    [4, 5, 6],
    7,
    [
        [
            8,
            [
                9, 
                10, 
                11,
                [12, 13, 14]
            ]
        ],
        [
            15,
            16,
            17, 
            18, 
            19,
            [
                20,
                21,
                22,
                [26, 27, 29]
            ],
            30,
            31
        ],
        32
    ],
    33
]

f_PrintNumbers(a)
```
