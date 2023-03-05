def radix_sort(arr):
    # find the maximum number to know the number of digits
    max_val = max(arr)
    
    # do counting sort for every digit
    exp = 1
    while max_val//exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    # initialize count array
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i]//exp) % 10
        count[index] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i]//exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] now
    # contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]
