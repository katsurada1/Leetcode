# time: O(1)
# n = len(s.split())
# space: O(n)

class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        """A function to return the length of the last word consisting of non-space characters in the string.
        Args:
            s (str): A given a string consisting of some words separated by some number of spaces.
        Returns:
            int: The length of the last word consisting of non-space characters in the string.
        """
        
        l = s.split()
        if l:
            return len(l[-1])
        
        else:
            return 0