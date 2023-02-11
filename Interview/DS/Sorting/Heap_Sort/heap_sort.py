def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    # Check if the left child of the root exists and is larger than the root
    if l < n and arr[l] > arr[largest]:
        largest = l
    # Check if the right child of the root exists and is larger than the root
    if r < n and arr[r] > arr[largest]:
        largest = r
    # Change the root if necessary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the affected sub-tree
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # Build a max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", heapSort(arr))
