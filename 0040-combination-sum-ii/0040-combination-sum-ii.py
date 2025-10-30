class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,cur_sum,path):
            if cur_sum==target:
                res.append(path)
                return
            if i>=len(candidates) or cur_sum>target:
                return
            # include the current
            dfs(i+1,cur_sum+candidates[i],path+[candidates[i]])
            # skip the current one
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,cur_sum,path)
        dfs(0,0,[])
        return res