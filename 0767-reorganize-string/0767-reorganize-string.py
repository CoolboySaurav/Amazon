import heapq
import collections

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(N) unique algo 
        charCount = Counter(s)
        maxCount, letter = 0, ""
        
        for c, cnt in charCount.items():
            if cnt > maxCount:
                maxCount = cnt
                letter = c
        
        if maxCount > (len(s) + 1) // 2:
            return ""
        
        ans = [""] * len(s)
        index = 0
        
        while charCount[letter] > 0:
            ans[index] = letter
            index += 2
            charCount[letter] -= 1
        
        
        for char, count in charCount.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                    
                ans[index] = char
                index += 2
                count -= 1
        return "".join(ans)
        
   
        
        # Neetcode easy to understand priority queue solution with tracking previous char
        
        maxHeap = [[- cnt, c] for c, cnt in Counter(s).items()]
        heapq.heapify(maxHeap)
        
        prev = None
        res = ""
        
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return res