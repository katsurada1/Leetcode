# n = len(nums)
# time:O(n)
# space:O(log(n))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """A fuction to convert an integer array nums where the elements are sorted in ascending order to a height-balanced binary search tree.
        Args:
            nums (List[int]): A given an integer array.
        Returns:
            TreeNode: A height-balanced binary search tree.
        """
        
        return self.recurse(0, len(nums) - 1, nums)

    def recurse(self, left, right, nums):
        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.recurse(left, mid - 1, nums)
        node.right = self.recurse(mid + 1, right, nums)
        return node