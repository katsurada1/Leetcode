# n = len(nums)
# time: O(n)
# space: O(1)

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        """A function to remove the duplicates in-place
        Args:
            nums (List[int]): A given an integer array nums sorted in non-decreasing order.
        Returns:
            int: The elements after removing the duplicates.
        """
        n = 0
        for i in range(len(nums)):
            if(nums[n] < nums[i]):
                n += 1
                nums[n] = nums[i]
        return n + 1