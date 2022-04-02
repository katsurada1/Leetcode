# n = len(nums)
# time: O(n)
# space: O(1)

class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        """A function to remove all occurrences of val in nums in-place.
        Args:
            nums (List[int]): A given an integer array.
            val (int): A given an integer.
        Returns:
            int: The elements after removing the elements equal to val.
        """
        
        n=0
        for i in nums:
            if i != val:
                nums[n] = i
                n += 1
        return n