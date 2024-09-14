class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxCount = 0
        countMap = defaultdict(int)
        for i in nums:
            countMap[i] += 1
            maxCount = max(maxCount, countMap[i])
        
        freq = [[] for i in range(maxCount + 1)]
        
        for n, f in countMap.items():
            freq[f].append(n)
        
        res=  []
        for i in range(maxCount, -1, -1):
            res.extend(freq[i])
            while len(res) > k:
                res.pop()
        return res