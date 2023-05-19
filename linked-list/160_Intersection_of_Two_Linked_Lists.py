# m = len(headA)
# n = len(headB)
# time: O(m + n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """A function to return the node at which the two lists intersect.
        Args:
            headA (ListNode):　A given the head of a linked list.
            headB (ListNode):　A given the head of a linked list.
        Return:
            Optional[ListNode]: The node at which the two lists intersect.
        """
        
        point_a = headA
        point_b = headB
        while point_a != point_b:
            if not point_a:
                point_a = headB
            else:
                point_a = point_a.next
            if not point_b:
                point_b = headA
            else:
                point_b = point_b.next
        return point_a