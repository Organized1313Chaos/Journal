import java.util.Arrays;

public class CountingSort {
    public static void main(String[] args) {
        int[] arr = {5, 1, 4, 2, 8};
        int[] sortedArray = countingSort(arr, 8);
        System.out.println("Sorted array: " + Arrays.toString(sortedArray));
    }

    /**
     * The main counting sort method that takes an array and the maximum value in the array as its arguments.
     * 
     * @param arr the array to be sorted
     * @param maxValue the maximum value in the array
     * @return the sorted array
     */
    public static int[] countingSort(int[] arr, int maxValue) {
        int[] count = new int[maxValue + 1];
        int[] sortedArray = new int[arr.length];

        // store count of each element
        for (int i = 0; i < arr.length; i++) {
            count[arr[i]]++;
        }

        // change count[i] so that count[i] now contains actual
        // position of this element in output array
        for (int i = 1; i <= maxValue; i++) {
            count[i] += count[i - 1];
        }

        // build the output array
        for (int i = arr.length - 1; i >= 0; i--) {
            sortedArray[count[arr[i]] - 1] = arr[i];
            count[arr[i]]--;
        }

        return sortedArray;
    }
}
