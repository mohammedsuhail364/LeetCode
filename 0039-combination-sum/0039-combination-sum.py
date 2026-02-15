class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,path,cur_sum):
            if i==len(candidates) or cur_sum>target:
                return
            if cur_sum==target:
                res.append(path)
                return
            dfs(i,path+[candidates[i]],cur_sum+candidates[i])
            dfs(i+1,path,cur_sum)
        dfs(0,[],0)
        return res