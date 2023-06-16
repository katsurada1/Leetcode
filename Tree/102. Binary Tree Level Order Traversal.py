# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = []
        queue.append(root)
        result = []
        while queue:
            level_size = len(queue)
            currentLevel_value = []
            for _ in range(level_size):
                node = queue.pop(0)
                currentLevel_value.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(currentLevel_value)
        return result