class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # refer neetcode
        minHeap=[1]
        factors=[2,3,5]
        visit=set([1])
        for i in range(n):
            num=heappop(minHeap)
            if i==n-1:
                return num
            for f in factors:
                if num*f not in visit:
                    visit.add(num*f)
                    heappush(minHeap,num*f)