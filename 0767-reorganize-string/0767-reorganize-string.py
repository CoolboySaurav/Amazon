import heapq
import collections

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Count frequency of each character
        counter = collections.Counter(s)
        heap = []
        
        # Step 2: Push characters into a max-heap based on their frequency
        for c, v in counter.items():
            heapq.heappush(heap, (-v, c))  # Using negative for max-heap behavior
        
        st = []
        
        # Step 3: Reorganize the string
        while len(heap) > 1:
            f1, a = heapq.heappop(heap)  # Most frequent character
            f2, b = heapq.heappop(heap)  # Second most frequent character
            
            # Add these characters to the result
            st.append(a)
            st.append(b)
            
            # Decrement the frequencies
            f1 += 1
            f2 += 1  # Incrementing because we use negative frequencies
            
            # If there's still remaining frequency for a character, push it back
            if f1 < 0:
                heapq.heappush(heap, (f1, a))
            if f2 < 0:
                heapq.heappush(heap, (f2, b))
        
        # Step 4: Handle the last character, if any
        if heap:
            f, last_char = heapq.heappop(heap)
            if -f > 1:
                return ""  # Impossible to reorganize
            st.append(last_char)
        
        return "".join(st)
