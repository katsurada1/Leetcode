# Two pointers

# n = len(head)
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """A function to determine if the linked list has a cycle in it.
        Args:
            head (Optional[ListNode]):　A given the head of a linked list.
        Return:
            bool: There is a cycle in the linked list or not.
        """
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# # dict

# # n = len(head)
# # time: O(n)
# # space: O(n)

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         """A function to determine if the linked list has a cycle in it.
#         Args:
#             head (Optional[ListNode]):　A given the head of a linked list.
#         Return:
#             bool: There is a cycle in the linked list or not.
#         """
        
#         hashmap = {}
#         while head:
#             if head in hashmap:
#                 return True
#             hashmap[head] = head
#             head = head.next