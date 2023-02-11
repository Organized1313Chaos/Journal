'''
NOTES:
Time Complexity: O(N^2)
Space Complexity: O(1) [temp for swapping]
'''

def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop runs n times
    for i in range(n):
        
        # Inner loop runs n-i-1 times
        for j in range(0, n-i-1):
            
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    # Return the sorted list
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting: ", arr)
arr = bubble_sort(arr)
print("After sorting: ", arr)
