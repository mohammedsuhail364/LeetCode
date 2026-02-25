class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        # 1 1 2 5 6 7 10
        def dfs(i,path,cur_sum):
            if cur_sum==target:
                res.append(path)
                return
            if i>=len(nums) or cur_sum>target:
                return
            # include the current one
            dfs(i+1,path+[nums[i]],cur_sum+nums[i])
            # skip the current one
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,path,cur_sum)
            
        dfs(0,[],0)
        return res