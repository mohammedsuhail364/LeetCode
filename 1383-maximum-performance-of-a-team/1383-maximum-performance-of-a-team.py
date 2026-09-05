class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # refer neetcode
        minHeap=[]
        performance=[(e,s) for s,e in zip(speed,efficiency)]
        performance.sort(reverse=True)
        totalSpeed=0
        res=0
        for i in range(len(performance)):
            if len(minHeap)==k:
                x = heappop(minHeap)
                totalSpeed-=x
            e,s = performance[i]
            totalSpeed+=s
            heappush(minHeap,s)
            total=totalSpeed*e
            res=max(res,total)
        return res%(10**9+7)