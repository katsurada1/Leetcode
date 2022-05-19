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
        
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            
            elif x < mid ** 2:
                high = mid - 1
            else:
                low = mid + 1