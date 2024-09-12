class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxSoFar = 0
        
        for i, v in enumerate(nums):
            if i > maxSoFar:
                return False
            maxSoFar = max(maxSoFar, i + v)
        return True