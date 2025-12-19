class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        last_index=defaultdict(list)
        res=[]
        for i,val in enumerate(nums):
            last_index[val].append(i)
        for i in queries:
            if len(last_index[x])<i:
                res.append(-1)
            else:
                res.append(last_index[x][i-1])
        return res