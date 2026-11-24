class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res=[]
        def dfs(cur):
            if cur>n:return 
            res.append(cur)
            for d in range(10):
                dfs(cur*10+d)
        for start in range(1,10):
            dfs(start)
        return res