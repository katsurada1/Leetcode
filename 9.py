# n = log10(x)
# time: O(n)
# space: O(1)

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        """A function to return true if x is palindrome integer.
        Args:
            x (int): A given integer.
        Returns:
            bool: True if x is palindrome integer.
        """

        if x < 0:
            return False
        
        number = x
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        return x == reverse