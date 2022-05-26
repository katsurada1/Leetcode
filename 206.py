# n = len(head)
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """A function to reverse a singly linked list.
        Args:
            head (Optional[ListNode]):　A given a linked list.
        Return:
            Optional[ListNode]: A reversed linked list.
        """
        
        while head:
            temp = head
            pre = None
            while temp:
                nex = temp.next
                temp.next = pre
                pre = temp
                temp = nex
            return pre