class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        minLen = float("inf")
        
        for s in strs:
            minLen = min(minLen, len(s))
        
        i = 0
        while i < minLen:
            ch = strs[0][i]
            for s in strs[1:]:
                if ch != s[i]:
                    return strs[0][:i]
            i += 1
        return strs[0][: minLen]
        
        
      
        
        
        if not strs:
            return ''
        minlen = float('inf')
        for s in strs:
            minlen = min(minlen, len(s))
        i = 0
        while i < minlen:
            ch = strs[0][i]
            for s in strs[1:]:
                if i < len(s) and ch != s[i]:
                    return strs[0][:i]
            i += 1
        return strs[0][:minlen] ## Case where lets say len of 1st string > 2nd string
        