class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s='abc'
        self.res=[]
        def backtrack(i,res):
            if i==n:
                self.res.append(res.copy())
                return
            for x in s:
                if res and res[-1]==x:
                    continue
                res.append(x)
                backtrack(i+1,res)
                res.pop()
        backtrack(0,[])
        if k>len(self.res):
            return ''
        res=self.res[k-1]
        return ''.join(res)