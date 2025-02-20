import numpy as np
class MedianFinder:

    def __init__(self):
        self.li=[]

    def addNum(self, num: int) -> None:
        self.li.append(num)

    def findMedian(self) -> float:
        self.li.sort()
        if len(self.li)%2==0:
            mid=len(self.li)//2
            value=(self.li[mid-1]+self.li[mid])/2
            return value

        else:
            mid=len(self.li)//2

            return self.li[mid]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()