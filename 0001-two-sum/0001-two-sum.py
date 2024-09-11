class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = defaultdict(int)
        
        for i, v in enumerate(nums):
            if (target - v) in numMap:
                return [numMap[(target - v)], i]
            numMap[v] = i