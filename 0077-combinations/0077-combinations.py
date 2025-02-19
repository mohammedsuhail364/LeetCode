class Solution:
    def combine(self, n: int, k: int) :
        self.res=[]
        nums=[i for i in range(1,n+1)]
        def backtrack(i,res):
            if i==k:
                self.res.append(res.copy())
                return
            for x in nums:
                if res and res[-1]>=x:
                    continue
                res.append(x)
                backtrack(i+1,res)
                res.pop()

        backtrack(0,[])
        return self.res