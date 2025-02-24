class Solution:
    def combinationSum2(self, candidates, target: int):
        self.res=[]
        candidates.sort()
        def backtrack(start,res,cur_sum):
            if cur_sum==target:
                self.res.append(res[:])
                return 
            if cur_sum>target:
                return 
            for x in range(start,len(candidates)):
                if x>start and candidates[x]==candidates[x-1]:
                    continue
                res.append(candidates[x])
                backtrack(x+1,res,cur_sum+candidates[x])
                res.pop()
                
        backtrack(0,[],0)
        return self.res