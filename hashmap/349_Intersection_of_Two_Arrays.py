# time: O(m + n)
# space: O(n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        result = []
        for index in nums1:
            hashmap[index] = 1
        for index in nums2:
            if index in hashmap and hashmap[index]:
                result.append(index)
                hashmap[index] -=1
        return result
