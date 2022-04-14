# n = len(nums)
# time: O(n)
# space: O(1)

class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        """A function to find the contiguous subarray which has the largest sum.
        Args:
            nums (List[int]): A given an integer array.
        Returns:
            int: The sum of the contiguous subarray which has the largest sum.
        """
        
        res = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            res = max(res, nums[i])
        return res