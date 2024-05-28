# Chapter 20

## Exercise 06

You're writing a function that accepts an array of unsorted integers and returns the length of the longest consequtive sequence among them. The sequence is formed by integers that increase by 1.  

If we sorted the array, we can then traverse the array just once to find the longest consequtive sequence. However, the sorting itself would take $O\left(N \log(N)\right)$. Your job is to optimize the function so that it takes $O(N)$ time.

```python
def ConsSqeqLen(array):
    d = {}
    max_len = 0

    for a in array:
        d[a] = True
    
    for a in array:
        if (a - 1) not in d:
            current_len = 1
            current_numb = a

            while (current_numb + 1) in d:
                current_len +=1
                current_numb += 1
                
                if current_len > max_len:
                    max_len = current_len
    
    return max_len


a = [19, 13, 15, 12, 18, 14, 17, 11]
print(ConsSqeqLen(a))
```