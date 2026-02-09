class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # can we solve with two different approach 
        # 1. using heap
        # 2. using sweep line but in this using so many imports(not built-in) thats why i m prefer the heap solution
        people=[(p,i) for i,p in enumerate(people)]
        flowers.sort()
        end=[]
        count=0
        res=[0]*len(people)
        j=0
        for p,i in sorted(people):
            while j<len(flowers) and flowers[j][0]<=p:
                heappush(end,flowers[j][1])
                j+=1
            while end and end[0]<p:
                heappop(end)
            res[i]=len(end)
        return res