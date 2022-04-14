# n = log(x)
# time:O(n)
# space: O(1)

class Solution(object):
    def mySqrt(self, x: int) -> int:
        """A function to compute and return the square root of x.
        Args:
            x (int): A given a non-negative integer.
        Returns:
            int: The square root of x.
        """
        
        s = 0
        r = x
        while s <= r:
            mid = (s + r) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            
            elif x < mid * mid:
                r = mid - 1
            
            else:
                s = mid + 1