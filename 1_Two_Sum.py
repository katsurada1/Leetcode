# s = len(nums)
# time: O(s)
# space: O(s)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """A function to return indices of the two numbers such that they add up to target.
        Args:
            nums (List[int]): A given an array of integers.
            target (int): A given integer.
        Returns:
            List[int]: The indices of the two numbers such that they add up to target.
        """
        dict = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]],i]
                
            dict[nums[i]] = i