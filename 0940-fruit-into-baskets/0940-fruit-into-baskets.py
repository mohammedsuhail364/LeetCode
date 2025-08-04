class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res=0
        l=0
        di=defaultdict(int)
        for r in range(len(fruits)):
            di[fruits[r]]+=1
            while len(di)>2:
                di[fruits[l]]-=1
                if di[fruits[l]]==0:
                    del di[fruits[l]]
                l+=1
            res=max(res,r-l+1)
        return res
