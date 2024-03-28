# https://leetcode.com/problems/rotate-list/
# 61. Rotate List
# Given the head of a linked list, rotate the list to the right by k places.
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Runtime 38 ms
# Beats 56.88% of users with Python3
# Memory 16.60 MB
# Beats 89.16% of users with Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head: Optional[ListNode]):
        h = head
        cnt = 0
        while h != None:
            cnt += 1
            h = h.next

        return cnt


    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 0:
            return head

        l = self.getLength(head)
        # print(l)

        if l == 0:
            return head

        knew = k % l
        prek = l - knew
        rab = head
        cnt = 1
        while rab != None and cnt != prek:
            rab = rab.next
            cnt += 1
        
        tor = rab
        while rab.next != None:
            rab = rab.next

        # print(tor.val)
        # print(rab.val)
        rab.next = head
        temp = tor.next
        tor.next = None
        head = temp

        return head
