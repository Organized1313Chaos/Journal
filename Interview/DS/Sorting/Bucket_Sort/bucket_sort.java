import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BucketSort {
    public static void main(String[] args) {
        float[] arr = {0.897f, 0.565f, 0.656f, 0.1234f, 0.665f, 0.3434f};
        float[] sortedArray = bucketSort(arr);
        for (float i : sortedArray) {
            System.out.println(i);
        }
    }

    /**
     * The main bucket sort method that takes an array of floating-point numbers as its argument.
     * 
     * @param arr the array to be sorted
     * @return the sorted array
     */
    public static float[] bucketSort(float[] arr) {
        List<Float>[] buckets = new List[arr.length];

        // initialize buckets
        for (int i = 0; i < arr.length; i++) {
            buckets[i] = new ArrayList<>();
        }

        // distribute the elements of the array into the buckets
        for (float i : arr) {
            int bucketIndex = (int)(arr.length * i);
            buckets[bucketIndex].add(i);
        }

        // sort the elements in each bucket
        for (List<Float> bucket : buckets) {
            Collections.sort(bucket);
        }

        // concatenate the sorted elements from each bucket into a single array
        int index = 0;
        for (List<Float> bucket : buckets) {
            for (float i : bucket) {
                arr[index++] = i;
            }
        }

        return arr;
    }
}
