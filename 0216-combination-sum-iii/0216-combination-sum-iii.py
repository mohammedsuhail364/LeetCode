class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dfs(i,path,cur_sum):
            if len(path)>k:
                return
            if cur_sum==n and len(path)==k:
                res.append(path)
                return
            if i>9 or cur_sum>n:
                return
            # include the current one 
            dfs(i+1,path+[i],cur_sum+i)
            # skip the current one
            dfs(i+1,path,cur_sum)
        dfs(1,[],0)
        return res