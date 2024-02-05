# https://leetcode.com/problems/add-two-numbers-ii/description/
# 445. Add Two Numbers II

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# Example 3:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Runtime 47 ms
# Beats 96.01% of users with Python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

        
    def findLen(self, l1):
        cnt = 0
        h = l1
        if h is None:
            return cnt

        while h is not None:
            # print(h.val)
            cnt += 1
            h = h.next
        return cnt

    def rev_list(self, l1):
        p = l1
        n = l1.next
        p.next = None

        while n is not None:
            # print(p.val, n.val)
            t = n.next
            n.next = p
            p = n
            n = t

        return p


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        rl1 = self.rev_list(l1)
        # print(rl1)

        rl2 = self.rev_list(l2)
        # print(rl2)

        ln1 = self.findLen(rl1)
        # print(ln1)
        ln2 = self.findLen(rl2)
        # print(ln2)

        minl = ln1
        if ln1 > ln2:
            minl = ln2

        cnt = 0
        op = None
        h1 = rl1
        h2 = rl2
        carry = 0
        while h1 is not None and h2 is not None:    
            cnt += 1
            n1 = h1.val
            n2 = h2.val
            s = ListNode()
            sm = n1+n2+carry
            s.val = sm%10
            carry = sm//10
            # print("sum",cnt,n1,n2,sm,carry,s)
            if op is None:
                op = s
            else:
                s.next = op
                op = s
            h1 = h1.next
            h2 = h2.next

        # print(h1,h2,carry)
        if h1 is not None:
            while h1 is not None or carry != 0:
                s = ListNode()
                n = 0
                if h1 is not None:
                    n = h1.val
                    h1 = h1.next
                sm = carry + n
                s.val = sm%10
                carry = sm//10
                s.next = op
                op = s
        elif h2 is not None:
            while h2 is not None or carry != 0:
                s = ListNode()
                n = 0
                if h2 is not None:
                    n = h2.val
                    h2 = h2.next
                sm = carry + n
                s.val = sm%10
                carry = sm//10
                s.next = op
                op = s
                
        else:
            if carry != 0:
                s = ListNode()
                s.val = carry
                s.next = op
                op = s

        # print(op)
        return op


        
        