class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = float('-inf')
        curSum = 0
        for num in nums:
            curSum += num
            maxSum = max(maxSum, curSum)
            curSum = max(curSum, 0)
        return maxSum