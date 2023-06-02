# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return None

        if not root.left and not root.right:
            return root.val == targetSum

        left_sum = targetSum - root.val
        if root.left and self.hasPathSum(root.left, left_sum):
            return True
    
        right_sum = targetSum - root.val
        if root.right and self.hasPathSum(root.right, right_sum):
            return True
        
        return False