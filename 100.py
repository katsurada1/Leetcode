# n = max{len(p), len(q)}
# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """A function to to check if the roots of two binary trees are the same or not.
        Args:
            p (TreeNode): A given the roots of a binary tree.
            q (TreeNode): A given the roots of a binary tree.
        Return:
            bool: The roots of two binary trees are the same or not.
        """
        
        if not p and not q:
            return True
        
        elif not p or not q:
            return False
        
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        else:
            return False