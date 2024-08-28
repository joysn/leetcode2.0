# https://leetcode.com/problems/reverse-linked-list-ii

# Runtime 31 ms Beats 82.26%
# Memory 16.49 MB Beats 97.75%

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        pos = 1
        head_sublist = head
        tail = None
        while pos < left:
            pos += 1
            tail = head_sublist
            head_sublist = head_sublist.next

        # print(tail,head_sublist)

        prev = None
        curr = head_sublist
        
        while pos <= right:
            pos += 1
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if tail is not None:
            tail.next = prev
        else:
            head = prev
        head_sublist.next = curr

        return head
