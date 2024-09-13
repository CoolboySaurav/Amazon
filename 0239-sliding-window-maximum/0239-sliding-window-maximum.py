class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = deque()
        l = r = 0
        
        while r < len(nums):
            # Storing elements inside q in decreasing order such that q[0] will be the max element of that window
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if q[0] < l:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res