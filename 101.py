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
        
        # if not root:
        #     return False
        
        # stack = deque([(root.left, root.right)])
        # while stack:
        #     left_node, right_node = stack.pop()
        #     if not left_node and not right_node:
        #         continue
            
        #     if not left_node or not right_node:
        #         return False
            
        #     if left_node.val != right_node.val:
        #         return False
                
        #     stack.append((left_node.left, right_node.right))
        #     stack.append((left_node.right, right_node.left))
        # return True
            