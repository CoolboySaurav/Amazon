class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        center = (m + n + 1) / 2
        l, r = 0, m
        N = m + n
        while l <= r:
            mid1 = l + (r - l) // 2
            mid2 = center - mid1
            l1 = l2 = float('-inf')
            r1 = r2 = float('inf')
            if mid1 < m:
                r1 = nums1[mid1]
            if mid2 < n:
                r2 = nums2[mid2]
            if mid1 > 0:
                l1 = nums1[mid1 - 1]
            if mid2 > 0:
                l2 = nums2[mid2 - 1]
            
            if l1 <= r2 and l2 <= r1:
                if N % 2:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0 
            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1
        

        
        