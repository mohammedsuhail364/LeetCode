class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def helper(i):
            di=defaultdict(int)
            for x,y in zip(tops,bottoms):
                if x==i or y==i:
                    di[i]+=1
            res=inf
            for i,j in di.items():
                if j==len(tops):
                    top=tops.count(i)
                    bottom=bottoms.count(i)
                    if top>bottom:
                        res=min(res,len(tops)-top)
                    elif top<=bottom:
                        res=min(res,len(tops)-bottom)
            return -1 if res==inf else res
        res=helper(tops[0])
        if res!=-1:
            return res
        return helper(bottoms[0])