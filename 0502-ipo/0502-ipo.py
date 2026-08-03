class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # this question was a classic two heap problem 
        # one heap is used for get the capital,profit values which has less than or equal to w
        # get that profits and push in the another heap and at finally get the maximum value from that
        maxHeap=[]
        minHeap=[]
        for c,p in zip(capital,profits):
            heappush(minHeap,(c,p))
        for i in range(k):
            while minHeap and minHeap[0][0]<=w:
                c,p=heappop(minHeap)
                heappush_max(maxHeap,p)
            if not maxHeap:
                break
            w+=heappop_max(maxHeap)
        return w