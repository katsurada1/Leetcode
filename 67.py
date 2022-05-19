# n = max(len(a) + 1, len(b) + 1)
# time: O(n)
# space: O(n)

class Solution(object):
    def addBinary(self, a: str, b: str) -> str:
        """A function to return sum of two binary strings as a binary string.
        Args:
            a (str): A given a binary string.
            b (str): A given a binary string.
        Returns:
            str: A binary string of sum of two binary strings.
        """
        
        i, j = len(a)-1, len(b)-1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res.append(str(carry % 2))
            carry //= 2
        return "".join(res[::-1])