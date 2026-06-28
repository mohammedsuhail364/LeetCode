class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=0
        def dfs(i,cur_sum):
            nonlocal res
            if i>=len(nums):
                res+=cur_sum
                return
            # skip the current one 
            dfs(i+1,cur_sum)
            # include the current one
            dfs(i+1,cur_sum^nums[i])
        dfs(0,0)
        return res