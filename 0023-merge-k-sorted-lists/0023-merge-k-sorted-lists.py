# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                element = [lists[i].val, lists[i]]
                heapq.heappush(heap, element)
        
        temp = dummy = ListNode(0)
        
        while heap:
            val, node = heapq.heappop(heap)
        
            temp.next = node
            if node.next:
                element = [node.next.val, node.next]
                heapq.heappush(heap, element)
            temp = temp.next 
        
        return dummy.next