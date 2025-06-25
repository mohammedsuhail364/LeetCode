class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        res=[]
        for i,j in c.items():
            heappush(res,(-j,i))
        ans=[]
        for x in range(k):
            j,i=heappop(res)
            ans.append(i)
        return ans