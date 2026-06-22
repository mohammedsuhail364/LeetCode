class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen=defaultdict(int)
        l=0
        res=0
        for r in range(len(fruits)):
            seen[fruits[r]]+=1
            while len(seen)>2:
                seen[fruits[l]]-=1
                if seen[fruits[l]]==0:
                    del seen[fruits[l]]
                l+=1
            res=max(res,r-l+1)
        return res