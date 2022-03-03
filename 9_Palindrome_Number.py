# n = len(x)
# time: O(n)
# space: O(n)

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        """A function to return true if x is palindrome integer.
        Args:
            x (int): A given integer.
        Returns:
            bool: True if x is palindrome integer.
        """

        if x < 0:
            return false
        reverse = 0
        i = x
        while i > 0:
            i //= 10
            reverse = reverse * 10 + i % 10
            return reverse
        
        if x == reverse:        
                return True