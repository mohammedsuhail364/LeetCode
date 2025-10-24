class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(i,path):
            if i>=len(nums):
                if path not in res:
                    res.append(path)
                return
            # skip the current one
            dfs(i+1,path)
            # include the current one
            for j in range(i,len(nums)):
                dfs(j+1,path+[nums[j]])
        res=[]
        dfs(0,[])
        return res