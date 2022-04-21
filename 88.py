# time: O(m + n)
# space: O(1)

class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """A function to merge two arrays into a single array sorted in non-decreasing order.
        Args:
            nums1 (List[int]): A given an integer array.
            m (int): A given the number of elements in nums1.
            nums2 (List[int]): A given an integer array.
            n (int): A given the number of elements in nums2.
        Returns:
            List[int]: A single array sorted in non-decreasing order merged nums1 and nums2 that be stored inside the array nums1.
        """
        
        while m and n:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        while n:
            nums1[n - 1] = nums2[n - 1]
            n -= 1