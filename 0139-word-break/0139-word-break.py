class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Tabulation
        n = len(s)
        dp = [False] * (n + 1)
        dictionary = set(wordDict)
        dp[n] = True
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i:j + 1] in dictionary:
                    if dp[j + 1]:
                        dp[i] = True
                        break
        
        return dp[0]
        
        
        # Memoization
        n = len(s)
        dp = [-1]*n
        dictionary = set(wordDict)
        
        def helper(ind):
            if ind == n:
                return True
            if dp[ind] != -1:
                return dp[ind]
            
            for i in range(ind, n):
                if s[ind:i+1] in dictionary:
                    if helper(i + 1):
                        dp[ind] = True
                        return dp[ind]
            dp[ind] = False
            return dp[ind]
        
        return helper(0)