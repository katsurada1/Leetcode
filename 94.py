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
    def inorderTraversal(self, root: TreeNode):
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

    
    
    # def inorderTraversal(self, root: TreeNode):
    #     """A function to return the inorder traversal of nodes' values.
    #     Args: 
    #         root (TreeNode): A given a binary tree.
    #     Returns:
    #         List[int]: The inorder traversal of nodes' values.
    #     """
        
    #     res = []
    #     self.helper(root, res)
    #     return res
    
    # def helper(self, root, res):
    #     if root:
    #         self.helper(root.left, res)
    #         res.append(root.val)
    #         self.helper(root.right, res)
            
    
    # def inorderTraversal(self, root: TreeNode):
    #     """A function to return the inorder traversal of nodes' values.
    #     Args: 
    #         root (TreeNode): A given a binary tree.
    #     Returns:
    #         List[int]: The inorder traversal of nodes' values.
    #     """    
        
    #     res, stack = [], [(root, False)]
    #     while stack:
    #         node, visited = stack.pop()  
    #         if node:
    #             if visited:
    #                 res.append(node.val)
    #             else:  
    #                 stack.append((node.right, False))
    #                 stack.append((node, True))
    #                 stack.append((node.left, False))
    #     return res
         