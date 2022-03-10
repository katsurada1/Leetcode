# n = len(s)
# time: O(n)
# space: O(1)

class Solution(object):
    def isValid(self, s: str) -> bool:
        """A function to determine if the input string is valid.
        Args:
            s (str): A given a string containing just the characters '(', ')', '{', '}', '[' and ']'.
        Returns:
            bool: True if an input string is valid.
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []