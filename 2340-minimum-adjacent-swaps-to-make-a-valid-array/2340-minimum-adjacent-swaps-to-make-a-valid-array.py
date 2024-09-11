class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        
        # Initialize min and max variables
        minEle, minInd = float('inf'), 0
        maxEle, maxInd = float('-inf'), 0

        # Find minimum and maximum elements with their indices
        for i, v in enumerate(nums):
            if minEle > v:
                minEle = v
                minInd = i
            if maxEle <= v:
                maxEle = v
                maxInd = i

        # Calculate swaps needed
        count = 0

        # If max is not at the last position, we need to move it to the end
        count += (n - 1 - maxInd)
        # If min is not at the first position, we need to move it to the beginning
        count += minInd
        
        # If the min element is to the right of the max element
        if minInd > maxInd:
            count -= 1  # Reduce one swap as min moves before max

        return count
