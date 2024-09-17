class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st = []
        maxArea = - 1
        n = len(heights)
        
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                ind, height = st.pop()
                maxArea = max(maxArea, (height * (i - ind)))
                start = ind
            st.append([start, h])
        
        while st:
            ind, h = st.pop()
            maxArea = max(maxArea, (h*(n - ind)))
        
        return maxArea
        
        
        
        
        stack = []
        maxArea = -1
        n = len(heights)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                maxArea = max(maxArea, (height * (i - ind)))
                start = ind # We need to put i th smallest block at the earliest block smaller than ith block to calculate backward area as well
            stack.append([start, h])
        
        while stack:
            ind, height = stack.pop()
            maxArea = max(maxArea, (height * (n - ind)))
        
        return maxArea