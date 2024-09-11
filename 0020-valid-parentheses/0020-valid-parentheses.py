class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brack = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        stack = []
        
        for c in s:
            if c in {"(","[","{"}:
                stack.append(c)
            else:
                if not stack or (brack[c] != stack[-1]):
                    return False
                else:
                    stack.pop()
        return True if not stack else False