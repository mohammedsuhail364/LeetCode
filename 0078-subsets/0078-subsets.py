class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i,path):
            if i>=len(nums):
                res.append(path)
                return 
            # include the current one
            dfs(i+1,path+[nums[i]])
            # skip the current one
            dfs(i+1,path)
        dfs(0,[])
        return res