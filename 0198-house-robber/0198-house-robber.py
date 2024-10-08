class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        nxt = nxt2 = 0
        
        for i in range(n - 1, -1, -1):
            rob = dntrob = 0
            rob = nums[i] + nxt2
            dntrob = nxt
            cur = max(rob, dntrob)
            nxt2, nxt = nxt, cur
        return nxt
        
        
        
        dp = [0] * (n + 2)
        
        for ind in range(n - 1, -1, -1):
            rob = dontRob = float('-inf')
            
            rob = nums[ind] + dp[ind + 2]
            dontRob = dp[ind + 1]
            dp[ind] = max(rob, dontRob) 
        
        return dp[0]

        
        dp = [-1] * (n)
        def helper(ind):
            if ind >= n:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]
            
            rob = dontRob = float('-inf')
            
            rob = nums[ind] + helper(ind + 2)
            dontRob = helper(ind + 1)
            dp[ind] = max(rob, dontRob) 
            
            return dp[ind]
        
        return helper(0)