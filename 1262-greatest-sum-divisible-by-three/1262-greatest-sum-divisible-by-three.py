class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,remain):
            if i>=len(nums):
                if remain%3==0:
                    return 0
                return -inf
            # skip the current one
            skip=dfs(i+1,remain)
            # include the current one
            include=nums[i]+dfs(i+1,(remain+nums[i])%3)
            return max(skip , include)
        return dfs(0,0)
