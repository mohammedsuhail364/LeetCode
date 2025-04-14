class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=Counter(nums)
        res=[]
        for i,j in n.items():
            res.append((j,i))
        res.sort(reverse=True)
        final_res=[]
        for i in range(k):
            x,y=res[i]
            final_res.append(y)
        return final_res