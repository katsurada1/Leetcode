from collections import deque

# n = len(root)
# time: O(n)
# space: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSymmetric(self, root: TreeNode) -> bool:
        """A function to check whether a binary tree is a mirror of itself.
        Args:
            root (TreeNode): A given a binary tree.
        Returns:
            bool: Whether a binary tree is a mirror of itself.
        """
        
        if not root:
            return True
        return self.check(root.left, root.right)
        
    def check(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        if left.val != right.val:
            return False
        
        return self.check(left.left, right.right) and self.check(left.right, right.left)
        

# time: O(n)
# space: O(n)
        
    # def isSymmetric(self, root):
    #     """A function to check whether a binary tree is a mirror of itself.
    #     Args:
    #         root (TreeNode): A given a binary tree.
    #     Returns:
    #         bool: Whether a binary tree is a mirror of itself.
    #     """
        
    #     if not root:
    #         return False
        
    #     stack = collections.deque[(root.left, root.right)]
    #     while stack:
    #         l, r = stack.pop()
    #         if not l and not r:
    #             pass
            
    #         elif not l or not r:
    #             return False
            
    #         else:
    #             if l.val != r.val:
    #                 return False
                
    #             stack.append((l.left, r.right))
    #             stack.append((l.right, r.left))
    #     return True
            
            