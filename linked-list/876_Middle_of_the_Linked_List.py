# n = len(head)
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """A function to determine the middle node of the linked list.
        Args:
            head (Optional[ListNode]):　A given a linked list.
        Return:
            Optional[ListNode]: The middle node of the linked list.
        """
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        