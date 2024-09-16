# n = len(s)
# time: O(n)
# space: O(n)

class Solution(object):
    def isValid(self, s: str) -> bool:
        """A function to determine if the input string is valid.
        Args:
            s (str): A given a string containing just the characters '(', ')', '{', '}', '[' and ']'.
        Returns:
            bool: True if an input string is valid.
        """
        stack = deque()
        k_dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in k_dict.values():
                stack.append(char)
            elif char in k_dict.keys():
                if stack == deque() or k_dict[char] != stack.pop():
                    return False
                
            else:
                return False
            
        return stack == deque()