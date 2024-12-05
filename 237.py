# time: O(1)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """A function to delete a node in a singly-linked list.
            node:　A given node to be deleted.
        """
        
        node.val = node.next.val
        node.next = node.next.next