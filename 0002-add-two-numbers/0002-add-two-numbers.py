# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode()
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            res = val1 + val2 + carry
            carry = res // 10
            prev.next = ListNode(res % 10)
            prev = prev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            prev.next = ListNode(carry)
        return dummy.next
            
            
    
        
        
        