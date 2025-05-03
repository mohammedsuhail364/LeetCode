from collections import defaultdict

class Solution:
    def minDominoRotations(self, tops, bottoms) -> int:
        def helper(i):
            di=defaultdict(int)
            
            for x , y in zip(tops,bottoms):
                if x==i or y==i:
                    di[i]+=1
            res=float('inf')
            for i, j in di.items():
                if j==len(tops):
                    if tops.count(i)>bottoms.count(i):
                        res=min(len(tops)-tops.count(i),res)
                    elif tops.count(i)<=bottoms.count(i):
                        res=min(len(tops)-bottoms.count(i),res)
            return res if res != float('inf') else -1
        res=helper(tops[0])
        if res!=-1:
            return res
        return helper(bottoms[0])
        
        