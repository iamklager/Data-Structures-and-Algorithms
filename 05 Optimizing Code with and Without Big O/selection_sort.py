def selectionSort (array):
    for i in range(len(array)):
        lowestNumberIndex = i
        
        for j in range(i + 1, len(array)):
            if array[j] < array[lowestNumberIndex]:
                lowestNumberIndex = j
        
        if lowestNumberIndex != i:
            temp = array[i]
            array[i] = array[lowestNumberIndex]
            array[lowestNumberIndex] = temp
    
    return array

print(selectionSort([4, 2, 7, 1, 3]))
