class MedianFinder:

    def __init__(self):
        # this question basically use the two heap pattern 
        # one heap contains the lower half with negatives 
        # another heap contains the upper half with positives
        self.maxHeap=[]  #lower half with negatives 
        self.minHeap=[] # upper half with positives

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap,-num)
        heappush(self.minHeap,-heappop(self.maxHeap))
        if len(self.minHeap)>len(self.maxHeap):
            heappush(self.maxHeap,-heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap)>len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0]+self.minHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()