# n = len(s)
# time: O(n)
# space: O(n)

class Solution(object):
    def romanToInt(self, s: str) -> int:
        """A function to  convert a roman numeral to an integer.
        Args:
            s (str): A given roman numeral.
        Returns:
            int: An intger corresponding to a roman numeral.
        """
    
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
        