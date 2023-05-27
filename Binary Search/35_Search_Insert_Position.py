# time: O(logn)
# space: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) 
        while left < right:
            mid = (right + left ) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
