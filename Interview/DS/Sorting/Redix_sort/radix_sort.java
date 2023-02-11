public class RadixSort {
    public static void main(String[] args) {
        int[] arr = {4725, 4586, 1330, 8792, 1594, 5729};
        radixSort(arr, 10, 4);
        for (int i : arr) {
            System.out.println(i);
        }
    }

    /**
     * The main radix sort method that takes an array of integers, the number of digits in the largest number in the array,
     * and the radix as its arguments.
     * 
     * @param arr the array to be sorted
     * @param radix the base of the number system used for sorting
     * @param width the number of digits in the largest number in the array
     */
    public static void radixSort(int[] arr, int radix, int width) {
        for (int i = 0; i < width; i++) {
            radixSingleSort(arr, i, radix);
        }
    }

    /**
     * A helper method that performs a single pass of the radix sort algorithm.
     * 
     * @param arr the array to be sorted
     * @param position the digit position to be considered in this pass
     * @param radix the base of the number system used for sorting
     */
    public static void radixSingleSort(int[] arr, int position, int radix) {
        int numItems = arr.length;
        int[] countArray = new int[radix];

        for (int value : arr) {
            countArray[getDigit(position, value, radix)]++;
        }

        // Adjust the count array
        for (int j = 1; j < radix; j++) {
            countArray[j] += countArray[j - 1];
        }

        int[] temp = new int[numItems];
        for (int tempIndex = numItems - 1; tempIndex >= 0; tempIndex--) {
            temp[--countArray[getDigit(position, arr[tempIndex], radix)]] = arr[tempIndex];
        }

        for (int tempIndex = 0; tempIndex < numItems; tempIndex++) {
            arr[tempIndex] = temp[tempIndex];
        }
    }

    /**
     * A helper method that returns the digit at a specified position for a given value.
     * 
     * @param position the digit position to return
     * @param value the value to consider
     * @param radix the base of the number system used for sorting
     * @return the digit at the specified position
     */
    public static int getDigit(int position, int value, int radix) {
        return value / (int) Math.pow(10, position) % radix;
    }
}
