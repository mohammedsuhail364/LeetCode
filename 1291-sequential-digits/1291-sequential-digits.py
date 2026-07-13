class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        def dfs(cur,prev):
            if (cur!="" and int(cur)>high) or prev>10:
                return 
            if cur!="" and low<=int(cur)<=high:
                res.append(int(cur))
            dfs(cur+str(prev),prev+1)
        for i in range(1,10):
            dfs("",i)
        return sorted(res)