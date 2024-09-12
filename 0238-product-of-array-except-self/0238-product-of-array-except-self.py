class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n=  len(nums)
        ans = [0] * n
        ans[0] = 1
        
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        R = 1
        
        for i in range(n - 1, -1, -1):
            ans[i] *= R
            R *= nums[i]
            
        
        return ans
        
        
        
        
        
        n = len(nums)
        left = [1] * n
        right= [1] * n
        
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        for i in range(n - 2, - 1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        for i in range(n):
            nums[i] = left[i] * right[i]
        
        return nums