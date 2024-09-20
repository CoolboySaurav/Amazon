class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        mod = 10**9 + 7
        
        # Arrays to store how far we can go left and right for each element
        left = [0] * n
        right = [0] * n
        
        # Stack for previous less element
        st = []
        
        # Calculate left bounds (number of subarrays ending at arr[i])
        for i in range(n):
            count = 1
            while st and arr[st[-1]] > arr[i]:
                count += left[st.pop()]
            left[i] = count
            st.append(i)
        
        # Clear stack for right calculation
        st = []
        
        # Calculate right bounds (number of subarrays starting at arr[i])
        for i in range(n - 1, -1, -1):
            count = 1
            while st and arr[st[-1]] >= arr[i]:
                count += right[st.pop()]
            right[i] = count
            st.append(i)
        
        # Total sum of subarray minimums
        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % mod
        
        return result
