class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c=Counter(arr)
        res=-1
        for i,j in c.items():
            if i==j:
                res=max(res,i)
        return res 