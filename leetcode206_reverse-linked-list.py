# https://leetcode.com/problems/reverse-linked-list/

# Runtime 40 ms Beats 37.54%
# Memory 17.64 MB Beats 81.11%

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        # print(head)
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            # print("Prev:",prev,"curr:", curr,"Temp:", temp)
            curr.next = prev
            prev = curr
            curr = temp
            # print("Prev:",prev,"curr:", curr,"Temp:", temp)
        
        return prev


        
