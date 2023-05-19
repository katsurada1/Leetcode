# n = len(head)
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = temp = ListNode(0, head)
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next
                
                
        