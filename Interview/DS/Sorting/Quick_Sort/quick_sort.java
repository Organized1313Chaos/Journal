import java.util.Arrays;

public class QuickSort {
    public static void main(String[] args) {
        int[] arr = {5, 1, 4, 2, 8};
        quickSort(arr, 0, arr.length - 1);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }

    /**
     * The main quicksort method that takes an array and two indices as its arguments.
     * 
     * @param arr the array to be sorted
     * @param low the lower index
     * @param high the higher index
     */
    public static void quickSort(int[] arr, int low, int high) {
        // if low is less than high, sort the sub-array
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            
            // sort elements before pivot
            quickSort(arr, low, pivotIndex - 1);
            // sort elements after pivot
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    /**
     * A helper method that takes an array and two indices as its arguments, and
     * selects a pivot element and rearranges the elements in the array so that
     * all elements smaller than the pivot are on one side and all elements larger
     * than the pivot are on the other side.
     * 
     * @param arr the array to be partitioned
     * @param low the lower index
     * @param high the higher index
     * @return the index of the pivot element
     */
    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high]; // select the last element as the pivot
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    /**
     * A helper method that takes an array and two indices as its arguments and
     * swaps the elements at the indices.
     * 
     * @param arr the array
     * @param i the first index
     * @param j the second index
     */
    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
