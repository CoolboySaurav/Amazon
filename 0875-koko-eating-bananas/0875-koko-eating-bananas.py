class Solution:
    def minEatingSpeed(self, piles, h):
        
        def solve(piles, k):
            time = 0
            for p in piles:
                time += p // k
                if p % k:
                    time += 1
                
            return time <= h
        
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            
            if solve(piles, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
        
        