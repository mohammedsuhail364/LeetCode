class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        di=defaultdict(int)
        res=0
        for i in dominoes:
            k=tuple(sorted(i))
            res+=di[k]
            di[k]+=1
        return res
            
