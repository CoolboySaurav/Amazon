class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temp)
        res = [0] * n
        st = []
        
        for i in range(n - 1, -1, -1):
            while st and temp[st[-1]] <= temp[i]:
                st.pop()
            if st:
                res[i] = st[-1] - i
            st.append(i)
            
        return res
        