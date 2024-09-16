class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        for j in range(1, len(nums)):
            if nums[pos] != nums[j]:
                pos += 1
                nums[pos] = nums[j]
        return pos + 1
    
    
        l = r = 0
        while r < len(nums):
            while (r < len(nums)) and nums[r] == nums[l]:
                r += 1
            l += 1
            if r >= len(nums):
                break
            nums[l] = nums[r]
        
        return l
            