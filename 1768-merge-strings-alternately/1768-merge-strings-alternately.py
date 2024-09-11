class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        l = r = 0
        
        while l < len(word1) or r < len(word2):
            if l < len(word1):
                res += word1[l]
                l += 1
            if r < len(word2):
                res += word2[r]
                r += 1
        return res
        