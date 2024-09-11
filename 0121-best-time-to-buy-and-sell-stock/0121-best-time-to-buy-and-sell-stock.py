class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        profit = 0
        
        for p in prices:
            if p < minPrice:
                minPrice = p
            profit = max(profit, p - minPrice)
        return profit