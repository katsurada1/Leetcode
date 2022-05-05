# n = len(root)
# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """A function to return the inorder traversal of nodes' values.
        Args: 
            root (TreeNode): A given a binary tree.
        Returns:
            List[int]: The inorder traversal of nodes' values.
        """

        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)