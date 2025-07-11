// Find the Median of two Sorted Arrays

public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // We are going to do the binary search look in the smallest array
        if (nums1.length > nums2.length) {
            // Swap to make sure nums1 is the smaller array
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        int m = nums1.length;
        int n = nums2.length;
        int total = m + n;
        // Number of elements that should be at the left of the median
        int half = total / 2;

        // Pointers for the small array
        int l = 0, r = m;

        // This will be valid only if left pointer is less or equal than right pointer
        while (l <= r) {
            // Partition for the nums1 array
            int i = (l + r) / 2;
            // Partition for the nums2 array (How many items are we missing?)
            int j = half - i;

            int left1 = (i > 0) ? nums1[i - 1] : Integer.MIN_VALUE;
            int right1 = (i < m) ? nums1[i] : Integer.MAX_VALUE;

            int left2 = (j > 0) ? nums2[j - 1] : Integer.MIN_VALUE;
            int right2 = (j < n) ? nums2[j] : Integer.MAX_VALUE;

            // We check if the current partition is valid:
            // All elements on the left side are less than or equal to those on the right side.
            if (left1 <= right2 && left2 <= right1) {
                if (total % 2 == 0) {
                    return (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
                } else {
                    return Math.min(right1, right2);
                }
            }
            // If left1 is greater than right2, we are too far to the right in nums1 so we move the cutoff to the left.
            else if (left1 > right2) {
                r = i - 1;
            }
            // If left2 is greater than right1, we are too far left in nums1 so we move the cut-off to the right.
            else {
                l = i + 1;
            }
        }

        
        throw new IllegalArgumentException("Input arrays are not valid.");
    }
}
