#time complexity (logn)
#space complexity O(n)
from heapq import *
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.small, -num)
            greater = -heappop(self.small)
            heappush(self.large, greater)

        else:
            heappush(self.large, num)
            smaller = heappop(self.large)
            heappush(self.small, -smaller)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            greater = -self.small[0]
            smaller = self.large[0]
            return float(greater + smaller)/2.0

        else:
            return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()