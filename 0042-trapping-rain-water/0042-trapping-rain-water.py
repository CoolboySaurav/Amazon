class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmax = rightmax = float('-inf')
        l, r = 0, len(height) - 1
        area = 0
        
        while r > l:
            leftmax = max(leftmax, height[l])
            rightmax= max(rightmax, height[r])
            area += leftmax - height[l]
            area += rightmax - height[r]
            if leftmax < rightmax:
                l += 1
            else:
                r -= 1
                
        return area