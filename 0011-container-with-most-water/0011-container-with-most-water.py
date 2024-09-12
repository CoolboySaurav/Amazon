class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxArea = -1
        while l < r:
            Base = r - l
            Height = min(height[l], height[r])
            maxArea = max(maxArea, (Base*Height))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea