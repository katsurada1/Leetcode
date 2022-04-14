# n = len(nums)
# time:O(log(n))
# space:O(1)

class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        """A function to  return the index if the target is found. If not, return the index where it would be if it were inserted in order.
        Args:
            nums (List[int]): A given a sorted array of distinct integers.
            target (int): A given an integer.
        Returns:
            int: The index if the target is found. If not, return the index where it would be if it were inserted in order.
        """
        r = 0
        s = len(nums) - 1
        while r <= s:
            mid = (r + s) // 2
            if nums[mid] < target:
                r = mid + 1
            elif nums[mid] == target:
                return mid
            
            else:
                s = mid - 1
        return r
            