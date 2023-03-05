import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args) {
        int[] arr = {5, 1, 4, 2, 8};
        bubbleSort(arr);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }

    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        
        // outer loop: iterates n-1 times
        for (int i = 0; i < n-1; i++) {
            
            // inner loop: iterates n-i-1 times
            for (int j = 0; j < n-i-1; j++) {
                
                // compare adjacent elements and swap if in wrong order
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}
