class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(cur_sum):
            if cur_sum in memo:
                return memo[cur_sum]
            if cur_sum==target:
                return 1
            if cur_sum>target:
                return 0
            memo[cur_sum]=0
            for x in nums:
                memo[cur_sum]+=dfs(cur_sum+x)
            return memo[cur_sum]       
        return dfs(0)