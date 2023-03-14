# Python program for Merge Sort

# Merges two subarrays of array[].
# First subarray is array[begin..mid]
# Second subarray is array[mid+1..end]
def merge(array, left, mid, right):
    subArrayOne = mid - left + 1
    subArrayTwo = right - mid

    # Create temp arrays
    leftArray = [0] * (subArrayOne)
    rightArray = [0] * (subArrayTwo)

    # Copy data to temp arrays leftArray[] and rightArray[]
    for i in range(0, subArrayOne):
        leftArray[i] = array[left + i]

    for j in range(0, subArrayTwo):
        rightArray[j] = array[mid + 1 + j]

    indexOfSubArrayOne = 0  # Initial index of first sub-array
    indexOfSubArrayTwo = 0  # Initial index of second sub-array
    indexOfMergedArray = left  # Initial index of merged array

    # Merge the temp arrays back into array[left..right]
    while (indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo):
        if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]):
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
        else:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1

        indexOfMergedArray += 1

    # Copy the remaining elements of left[], if there are any
    while (indexOfSubArrayOne < subArrayOne):
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
        indexOfSubArrayOne += 1
        indexOfMergedArray += 1

    # Copy the remaining elements of right[], if there are any
    while (indexOfSubArrayTwo < subArrayTwo):
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
        indexOfSubArrayTwo += 1
        indexOfMergedArray += 1

# begin is for left index and end is
# right index of the sub-array of arr to be sorted
def mergeSort(array, begin, end):
    if (begin >= end):
        return  # Returns recursively

    mid = begin + (end - begin) // 2
    mergeSort(array, begin, mid)
    mergeSort(array, mid + 1, end)
    merge(array, begin, mid, end)

# UTILITY FUNCTIONS
# Function to print an array
def printArray(A, size):
    for i in range(0, size):
        print(A[i], end=" ")

# Driver code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    arr_size = len(arr)

    print("Given array is")
    printArray(arr, arr_size)

    mergeSort(arr, 0, arr_size - 1)

    print("\nSorted array is")
    printArray(arr, arr_size)
