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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """A function to to check if the roots of two binary trees are the same or not.
        Args:
            p (TreeNode):　A given the roots of a binary tree.
            q (TreeNode):　A given the roots of a binary tree.
        Return:
            bool: The roots of two binary trees are the same or not.
        """
        
        if not p and not q:
            return True
        
        elif not p or not q:
            return False
        
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
        
        # def isSameTree(self, p, q):
        # """A function to to check if the roots of two binary trees are the same or not.
        # Args:
        #     p (TreeNode):　A given the roots of a binary tree.
        #     q (TreeNode):　A given the roots of a binary tree.
        # Return:
        #     bool: The roots of two binary trees are the same or not.
        # """
        
        # stack = [(p, q)]
        # while stack:
        #     p, q = stack.pop()
        #     if not p and not q: 
        #         pass
            
        #     elif not p or not q: 
        #         return False
            
        #     elif p.val != q.val: 
        #         return False
            
        #     else:
        #         stack.append((p.left, q.left))
        #         stack.append((p.right, q.right))
        # return True
