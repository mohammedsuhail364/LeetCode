class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        minHeap=[1]
        visit=set([1])
        for i in range(n):
            num=heappop(minHeap)
            if i==n-1:
                return num
            for p in primes:
                if num*p not in visit:
                    visit.add(num*p)
                    heappush(minHeap,num*p)