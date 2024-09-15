class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=len(nums)-2
        while l>=0:
            if nums[l+1]>nums[l]:
                break
            l-=1
        if l==-1:
            nums=nums.reverse()
            return nums
# 2 [4] 8 7 6 => 2 6 8 7 4 => 2 6 4 7 8
# 2 [4] 8 7 4 => 2 7 8 4 4 => 2 7 4 4 8 
        for i in range(len(nums)-1,l,-1):
            if nums[i]>nums[l]:
                nums[i],nums[l]=nums[l],nums[i]
                break
        nums[l+1:]=reversed(nums[l+1:])

        return nums

        