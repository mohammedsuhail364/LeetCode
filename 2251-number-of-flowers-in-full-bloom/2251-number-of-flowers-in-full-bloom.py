class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # can we solve with two different approach 
        # 1. using heap
        # 2. using sweep line but in this using so many imports(not built-in) thats why i m prefer the heap solution
        people=[(p,i) for i,p in enumerate(people)]
        start=[f[0] for f in flowers]
        end=[f[1] for f in flowers]
        heapify(start)
        heapify(end)
        count=0
        res=[0]*len(people)
        for p,i in sorted(people):
            while start and start[0]<=p:
                heappop(start)
                count+=1
            while end and end[0]<p:
                heappop(end)
                count-=1
            res[i]=count
        return res