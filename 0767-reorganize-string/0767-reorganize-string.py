import heapq
import collections

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
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