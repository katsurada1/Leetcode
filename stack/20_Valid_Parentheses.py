# n = len(s)
# time: O(n)
# space: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in hashmap:
                if not stack or stack.pop() != hashmap[char]:
                    return False
            else:
                stack.append(char)
        return not stack
