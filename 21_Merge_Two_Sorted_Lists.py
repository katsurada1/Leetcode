# n = len(l1)
# m = len(l2)
# time: O(n + m)
# space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """A function to merge the two lists in a one sorted list
        Args:
            l1 (Optional[ListNode]): A given the heads of sorted linked list.
            l2 (Optional[ListNode]): A given the heads of sorted linked list.
        Returns:
            Optional[ListNode]: The head of the merged linked list made by splicing together the nodes of the first two lists.
        """
        
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            temp = head = ListNode(l1.val)
            l1 = l1.next
        else:
            temp = head = ListNode(l2.val)
            l2 = l2.next
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        while l1 is not None:
            temp.next = ListNode(l1.val)
            l1 = l1.next
            temp = temp.next
        while l2 is not None:
            temp.next = ListNode(l2.val)
            l2 = l2.next
            temp = temp.next
        return head