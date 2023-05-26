# time: O(n)
# space: O(n)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        result = -1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                result = i
                break
        return result