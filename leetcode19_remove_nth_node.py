# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
# Runtime: 61 ms, faster than 17.91% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.8 MB, less than 72.66% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        h = head
        t = head
        
        if n == 1 and h.next is None:
            return None

        print(h.val,t.val)
        cnt = 0
        while cnt<n:
            h = h.next
            cnt += 1
            
        if h is None:
            return t.next
        print(h.val,t.val)
        while h.next is not None:
            h = h.next
            t = t.next
        print(h.val,t.val)
        t.next = t.next.next
        
        return head
        