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
        
        res, stack = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res