class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i>=len(nums):
                return 0
            skip=dfs(i+1)
            include=nums[i]+dfs(i+2)
            memo[i]=max(skip,include)
            return memo[i]
        
        
        return dfs(0)