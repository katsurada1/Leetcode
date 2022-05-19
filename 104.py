# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

# recursive solution
# n = len(root)
# time: O(n)
# space: O(1)
    
    def maxDepth(self, root: TreeNode) -> int:
        """A function to return maximum depth of a binary tree.
        Args:
            root (TreeNode): A given a binary tree.
        Returns:
        int: The number of nodes along the longest path from the root node down to the farthest leaf node.
        """
        
        if not root:
            return 0

        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1


# # iterative solution
# # n = len(root)
# # time: O(n)
# # space: O(n)
    
#     def maxDepth(self, root: TreeNode) -> int:
#         """A function to return maximum depth of a binary tree.
#         Args:
#             root (TreeNode): A given a binary tree.
#         Returns:
#         int: The number of nodes along the longest path from the root node down to the farthest leaf node.
#         """
        
#         if not root:
#             return 0
        
#         depth = 1
#         queue = deque([(root, depth)])
#         while queue:
#             curr, val = queue.popleft()
#             if depth < val:
#                 depth = val
#             if curr.right:
#                 queue.append((curr.right, val + 1))
#             if curr.left:
#                 queue.append((curr.left, val + 1))
#         return depth


