# A class capable of sorting an array via quick sort and quick select.
class SortableArray:
    def __init__(self, array):
        self.array = array
    
    # Partioning function
    def Partition(self, ptr_l, ptr_r):
        i_pivot = ptr_r
        pivot = self.array[i_pivot]
        ptr_r -= 1
        
        while True:
            while self.array[ptr_l] < pivot:
                ptr_l += 1
            while self.array[ptr_r] > pivot:
                ptr_r -= 1
            
            if ptr_l >= ptr_r:
                break
            else:
                self.array[ptr_l], self.array[ptr_r] = self.array[ptr_r], self.array[ptr_l]
                ptr_l += 1
            
        self.array[ptr_l], self.array[i_pivot] = self.array[i_pivot], self.array[ptr_l]
        
        return ptr_l
        
    # Quick sort
    def QuickSort(self, i_l, i_r):
        if i_r <= i_l:
            return
        else:
            i_pivot = self.Partition(ptr_l = i_l, ptr_r = i_r)
            self.QuickSort(i_l = i_l, i_r = i_pivot - 1)
            self.QuickSort(i_l = i_pivot + 1, i_r = i_r)
    
    # Quick select
    def QuickSelect(self,  kth_low_val, i_l, i_r):
        if i_r <= i_l:
            return self.array[i_l]
        
        i_pivot = self.Partition(i_l, i_r)
        
        if kth_low_val < i_pivot:
            return self.QuickSelect(kth_low_val, i_l, i_pivot - 1)
        elif kth_low_val > i_pivot:
            return self.QuickSelect(kth_low_val, i_pivot + 1, i_r)
        else:
            return self.array[i_pivot]


a = [0, 5, 2, 1, 6, 3]
sa = SortableArray(array = a)
print("Original array: ", sa.array)
sa.QuickSort(i_l = 0, i_r = len(a) - 1)
print("Quick sort:     ", sa.array)
a = [0, 5, 2, 1, 6, 3]
sa = SortableArray(array = a)
print("Quick select (4th largest): ", sa.QuickSelect(kth_low_val = 3, i_l = 0, i_r = len(a) - 1))

