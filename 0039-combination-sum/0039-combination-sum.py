class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,path,cur_sum):
            if cur_sum==target:
                res.append(path)
                return 
            if cur_sum>target or i>=len(candidates):
                return
            # include the current one
            for j in range(i,len(candidates)):
                dfs(j,path+[candidates[j]],cur_sum+candidates[j])
        dfs(0,[],0)
        return res