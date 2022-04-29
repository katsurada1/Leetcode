# n = len(head)
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """A function to delete all duplicates in a sorted linked list.
        Args:
            head (ListNode): A given a sorted linked list.
        Returns:
            ListNode: A sorted linked list deleted all duplicates.
        """
        
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head