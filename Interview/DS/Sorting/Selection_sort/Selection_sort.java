import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = {5, 1, 4, 2, 8};
        selectionSort(arr);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }

    /**
     * The main selection sort method that takes an array as its argument.
     * 
     * @param arr the array to be sorted
     */
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            // swap arr[i] and arr[minIndex] if minIndex is not equal to i
            if (minIndex != i) {
                int temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
    }
}
