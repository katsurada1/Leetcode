# n = len(strs)
# k = max(strs[i])
# time: O(n * klogk)
# space: O(n)

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in hashmap:
                hashmap[sortedWord] = []
            hashmap[sortedWord].append(word)
        return list(hashmap.values())
