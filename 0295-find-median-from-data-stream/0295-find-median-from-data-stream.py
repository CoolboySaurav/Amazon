class MedianFinder(object):

    def __init__(self):
        self.small = [] # Max heap
        self.large = [] # Min heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, - num)
        
        if self.large and - self.small[0] > self.large[0]:
            number = - heapq.heappop(self.small)
            heapq.heappush(self.large, number)
            
        if len(self.small) > len(self.large) + 1:
            number = - heapq.heappop(self.small)
            heapq.heappush(self.large, number)
            
        if len(self.large) > len(self.small) + 1:
            number = - heapq.heappop(self.large)
            heapq.heappush(self.small, number)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return - self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return ((- self.small[0] + self.large[0]) / 2.0)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()