class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(i,cur_sum,path):
            if cur_sum==target:
                res.append(path)
                return 
            if cur_sum>target or i>=len(nums):
                return
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                dfs(j+1,cur_sum+nums[j],path+[nums[j]])
        dfs(0,0,[])
        return res