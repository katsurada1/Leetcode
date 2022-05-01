# time: O(n)
# space: O(1)

class Solution(object):
    def climbStairs(self, n: int) -> int:
        """A function to count the number of distinct way to climb a staircase to the top.
        Args:
            n (int): A given an integer indicating steps to reach the top.
        Returns:
            int: The numer of distinct way to climb to the top.
        """
        
        step1 = 1
        step2 = 1
        if n <= 0:
            return n
        
        for i in range(n):
            step1, step2 = step2, step1 + step2
        return step1