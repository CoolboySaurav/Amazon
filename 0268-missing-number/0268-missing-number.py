class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n
        
        for i, num in enumerate(nums):
            res += i - num
        return res