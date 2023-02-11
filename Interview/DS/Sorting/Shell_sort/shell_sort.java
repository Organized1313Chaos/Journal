public class ShellSort {
    public static void main(String[] args) {
        int[] arr = {20, 35, -15, 7, 55, 1, -22};
        shellSort(arr);
        for (int i : arr) {
            System.out.println(i);
        }
    }

    /**
     * The main shell sort method that takes an array of integers as its argument.
     * 
     * @param arr the array to be sorted
     */
    public static void shellSort(int[] arr) {
        int gap = arr.length / 2;
        while (gap > 0) {
            for (int i = gap; i < arr.length; i++) {
                int newElement = arr[i];

                int j = i;
                while (j >= gap && arr[j - gap] > newElement) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }

                arr[j] = newElement;
            }
            gap /= 2;
        }
    }
}
