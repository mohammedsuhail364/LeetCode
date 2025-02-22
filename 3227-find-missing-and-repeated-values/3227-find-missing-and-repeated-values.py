class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen=set()
        res=[]
        for i in grid:
            for y in i:
                if y not in seen:
                    seen.add(y)
                else:
                    res.append(y)
                    
        for x in range(1,len(seen)+2):
            if x not in seen:
                res.append(x)
                break
        return res
