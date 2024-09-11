class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = set()
        maxLen = 0
        l = i = 0
        
        for r in range(len(s)):
            while s[r] in charMap:
                charMap.remove(s[l])
                l += 1
            charMap.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen