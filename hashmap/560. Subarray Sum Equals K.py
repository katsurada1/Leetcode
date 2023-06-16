# time: O(n)
# space: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        count_map = {0: 1}
        for num in nums:
            current_sum += num
            if current_sum - k in count_map:
                count += 1
            if current_sum in count_map:
                count_map[current_sum] += 1
            else:
                count_map[current_sum] = 1
        return count




