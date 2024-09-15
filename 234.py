# n = len(head)
# time: O(n)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """A function to determine if a linked list is a palindrome.
            head (Optional[ListNode]):　A given a linked list.
        Return:
            bool: A linked list is a palindrome or not.
        """
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next    
        pre = None
        while slow:
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt
        while pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True