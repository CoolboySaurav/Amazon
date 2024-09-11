class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        """
        :type word: str
        :type forbidden: List[str]
        :rtype: int
        """
        dictionary = set()
        n = len(word)
        large_forbidden = 0
        
        for w in forbidden:
            dictionary.add(w)
            large_forbidden = max(large_forbidden, len(w))
        
        right = n - 1
        ans = 0
        for left in range(n - 1, -1, -1):
            for k in range(left, min(left + large_forbidden, right + 1)):
                if word[left: k + 1] in dictionary:
                    right = k - 1
                    break
            ans = max(ans, right - left + 1)
        return ans
        