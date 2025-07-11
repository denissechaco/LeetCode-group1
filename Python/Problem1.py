#### FIND MEDIAN OF SORTED ARRAYS ####

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #We are going to do the binary search look in the smallest array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        #number of elements that should be at the left of the median
        half = total // 2

        # Pointers for the small array
        l, r = 0, m

        # This will be valid only if left pointer is less or equal than right pointer
        while l <= r:
            #Partition for the nums1 array
            i = (l + r) // 2
            #Partition for the nums2 array (How many items are we missing?)
            j = half - i

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # We check if the current partition is valid:
            # All elements on the left side are less than or equal to those on the right side.
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return min(right1, right2)
            # If left1 is greater than right2, we are too far to the right in nums1 so we move the cutoff to the left.
            elif left1 > right2:
                r = i - 1
            # If left2 is greater than right1, we are too far left in nums1 so we move the cut-off to the right.
            else:
                l = i + 1
