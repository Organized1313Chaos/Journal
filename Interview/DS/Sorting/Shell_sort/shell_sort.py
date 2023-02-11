def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        # Do a gapped insertion sort for this gap size.
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                c1 = j - gap 
                c2 = arr[c1]
                
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Example code to run shell sort

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

shell_sort(arr)
print("Sorted array:", arr)
