class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res=0
        @lru_cache(None)
        def dfs(cur_sum):
            if cur_sum>target:
                return 0
            if target==cur_sum:
                return 1
            res=0
            for x in range(len(nums)):
                res+=dfs(cur_sum+nums[x])
            return res
        return dfs(0) 