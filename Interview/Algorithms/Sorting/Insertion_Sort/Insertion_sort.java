import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = {5, 1, 4, 2, 8};
        insertionSort(arr);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }

    /**
     * The main insertion sort method that takes an array as its argument.
     * 
     * @param arr the array to be sorted
     */
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            
            // move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }
}
