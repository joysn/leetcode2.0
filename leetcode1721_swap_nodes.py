# 1721. Swapping Nodes in a Linked List
# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]

# Runtime: 1465 ms, faster than 41.23% of Python3 online submissions for Swapping Nodes in a Linked List.
# Memory Usage: 48.5 MB, less than 57.32% of Python3 online submissions for Swapping Nodes in a Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        f = head
        # k = 1
        # removal of last node
        
        
        for i in range(1,k):
            f = f.next
        l = head
        e = f
        while e.next is not None:
            e = e.next
            l = l.next
            
        print(f.val,l.val)
        f.val,l.val = l.val,f.val
        
        return head