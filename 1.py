# n = len(nums)
# time: O(n)
# space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """A function to return indices of the two numbers such that they add up to target.
        Args:
            nums (List[int]): A given an array of integers.
            target (int): A given integer.
        Returns:
            List[int]: The indices of the two numbers such that they add up to target.
        """
        nums_dict = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num],i]
                
            nums_dict[num] = i