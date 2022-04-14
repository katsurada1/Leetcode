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
        
        temp = head = ListNode(0)
        
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    temp.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    temp.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next    
        return head.next