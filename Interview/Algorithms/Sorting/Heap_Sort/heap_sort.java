import java.util.Arrays;

public class HeapSort {
    public static void main(String[] args) {
        int[] arr = {5, 1, 4, 2, 8};
        heapSort(arr);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }

    /**
     * The main heap sort method that takes an array as its argument.
     * 
     * @param arr the array to be sorted
     */
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // build heap (rearrange array)
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // one by one extract an element from heap
        for (int i = n - 1; i >= 0; i--) {
            // move current root to end
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // call max heapify on the reduced heap
            heapify(arr, i, 0);
        }
    }

    /**
     * The heapify method that takes an array, its size, and the root node as its arguments.
     * 
     * @param arr the array to be heapified
     * @param n the size of the array
     * @param i the root node
     */
    public static void heapify(int[] arr, int n, int i) {
        int largest = i;
        //left Child
        int l = 2 * i + 1;
        //Right Child
        int r = 2 * i + 2;

        // if left child is larger than root
        if (l < n && arr[l] > arr[largest]) {
            largest = l;
        }

        // if right child is larger than largest so far
        if (r < n && arr[r] > arr[largest]) {
            largest = r;
        }

        // if largest is not root
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // recursively heapify the affected sub-tree
            heapify(arr, n, largest);
        }
    }
}
