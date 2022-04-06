# n = len(haystack) - len(needle) + 1
# m = len(needle)
# time: O(nm)
# space: O(1)

class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        """A function to return the index of the first occurrence of needle in haystack.
        Args:
            haystack (str): A given a string.
            needle (str): A given a string.
        Returns:
            int: The index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack, or 0 if needle is an empty string.
        """
        
        if len(needle) == 0:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j + 1 == len(needle):
                    return i
                
        return -1