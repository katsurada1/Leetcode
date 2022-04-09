# n = len(digits)
# time: O(n)
# space: O(1)

class Solution(object):
    def plusOne(self, digits: List[int]) -> List[int]:
        """A function to increment the integer by one and return the resulting array.
        Arg:
            digits (List[int]): A given an integer array.
        Returns:
            List[int]: The resulting array of digits that increment by one.
        """
        
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - 1 - i))
        return [i for i in str(num + 1)]