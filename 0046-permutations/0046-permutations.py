class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(path):
            if len(path)>=len(nums):
                res.append(path)
                return 
            for j in nums:
                if j in path:
                    continue
                dfs(path+[j])
        dfs([])
        return res
