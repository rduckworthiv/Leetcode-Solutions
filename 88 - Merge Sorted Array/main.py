class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # merge from end, starting from m+n-1
        last = m+n-1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:   # if nums1[m] <= nums2[n]
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        # if elements left in nums2, backfill nums1
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
        
