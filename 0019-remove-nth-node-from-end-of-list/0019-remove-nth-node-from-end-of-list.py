# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        dummy = ListNode(0, head)
        
        while n > 0:
            cur = cur.next
            n -= 1
        if not cur:
            return head.next
        while cur:
            cur = cur.next
            dummy = dummy.next 
        
        if dummy.next:
            dummy.next = dummy.next.next 
        return head