class Solution:
    def combine(self, n: int, k: int) :
        self.res=[]
        val=[i for i in range(1,n+1)]
        def backtrack(res,start):
            if len(res)==k:
                self.res.append(res.copy())
                return 
            for i in range(start,len(val)):
                res.append(val[i])
                backtrack(res,i+1)
                res.pop()
        backtrack([],0)
        return self.res