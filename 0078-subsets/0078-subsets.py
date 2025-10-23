class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i,path):
            if i==len(nums):
                res.append(path)
                return
            # skip the current
            dfs(i+1,path)
            # include the current 
            dfs(i+1,path+[nums[i]])
            
        dfs(0,[])
        return res