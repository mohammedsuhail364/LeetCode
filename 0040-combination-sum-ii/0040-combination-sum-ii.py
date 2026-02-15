class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,path,cur_sum):
            
            if cur_sum==target:
                res.append(path)
                return
            if i==len(candidates) or cur_sum>target:
                return
            # include the current one
            dfs(i+1,path+[candidates[i]],cur_sum+candidates[i])

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,path,cur_sum)

        dfs(0,[],0)
        return res
