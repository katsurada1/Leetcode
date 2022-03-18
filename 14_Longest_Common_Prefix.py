# n = len(s)
# time: O(n^2)
# space: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """A function to find the longest common prefix string amongst an array of strings.
        Args:
            strs (List[str]): A given an array of strings.
        Returns:
            str: The longest common prefix strings.
        """
        if not strs:
            return ""
        
        s = min(strs, key=len)
        for i, ch in enumerate(s):
            for other in strs:
                if other[i] != ch:
                    return s[:i]
        
        return s