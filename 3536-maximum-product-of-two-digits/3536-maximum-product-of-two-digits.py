class Solution:
    def maxProduct(self, n: int) -> int:
        heap=[]
        while n:
            t=n%10
            heappush(heap,t)
            if(len(heap))>2:
                heappop(heap)
            n=n//10
        return heappop(heap)*heappop(heap)