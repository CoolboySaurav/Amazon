class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Dynamic Programing Solution
        
        # Gap method tabulation with higher space usage (very important)
        n = len(s)
        dp = [[False]*n for _ in xrange(n)]
        count = 0
        curGap = -1
        start = end = 0
        
        for gap in xrange(n):
            for i in xrange(n - gap):
                j = i + gap
                
                if gap == 0:
                    dp[i][j] = True
                elif gap == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                if dp[i][j] and curGap < gap:
                    start= i
                    end = j
        
        return s[start:end+1]
           
        # Neetcode higher space optimised method
        res=""
        resLen=0

        for i in xrange(len(s)):
            #odd length
            l=r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=(r-l+1)
                l-=1
                r+=1
            #even length 
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=(r-l+1)
                l-=1
                r+=1
        return res