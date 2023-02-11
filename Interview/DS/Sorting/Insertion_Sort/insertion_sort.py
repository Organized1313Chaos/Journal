def insertionSort(arr):
    # loop through the array, starting from the second element
    for i in range(1, len(arr)):
        current_value = arr[i] # store the current value
        position = i # store the current position
        # move the elements of the sorted part of the array that are larger than the current value to the right
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        # insert the current value in the correct position
        arr[position] = current_value
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", insertionSort(arr))
