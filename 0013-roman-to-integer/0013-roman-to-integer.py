class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        charMap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000   
        }
        n = len(s)
        tot = 0
        for i in range(n - 1):        
            if s[i] == "I" and s[i + 1] in ("V", "X"):
                tot -= 1                
            elif s[i] == "X" and s[i + 1] in ("L", "C"):
                tot -= 10                
            elif s[i] == "C" and s[i + 1] in ("D", "M"):
                tot -= 100
            else:
                tot += charMap[s[i]]
        tot += charMap[s[n - 1]]
        return tot    