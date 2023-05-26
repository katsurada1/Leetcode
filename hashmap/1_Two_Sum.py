# time: O(n)
# space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in hashmap:
                return [i, hashmap[remaining]]
            else:
                hashmap[value] = i
