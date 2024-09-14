class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        wordDict = set(wordDict)
        res = []
        def helper(ind, path):
            if ind == n:
                res.append(" ".join(path))
                return 
            
            for i in range(ind, n):
                if s[ind : i + 1] in wordDict:
                    helper(i + 1, path + [s[ind : i + 1]])
        helper(0, [])
        return res