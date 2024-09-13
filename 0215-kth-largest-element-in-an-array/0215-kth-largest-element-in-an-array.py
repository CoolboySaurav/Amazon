class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        for num in nums:
            if len(pq) < k:
                heapq.heappush(pq, num)
            elif num > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, num)
        return pq[0]