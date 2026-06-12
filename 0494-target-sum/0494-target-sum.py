class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        total=sum(nums)
        offset=total
        if abs(target)>total:
            return 0
        size=2*total+1
        dp=[[0]*(size) for _ in range(n+1)]
        dp[n][target+offset]=1
        for i in range(n - 1, -1, -1):
            for cur in range(-total, total + 1):
                add_idx = (cur + nums[i]) + offset
                sub_idx = (cur - nums[i]) + offset
                add = dp[i+1][add_idx] if 0 <= add_idx < size else 0
                sub = dp[i+1][sub_idx] if 0 <= sub_idx < size else 0
                dp[i][cur + offset] = add + sub
        return dp[0][0+offset]
        # def dfs(i,cur):
        #     if (i,cur) in cache:
        #         return cache[i,cur]
        #     if i>=len(nums):
        #         if cur==target:
        #             return 1
        #         return 0
        #     add=dfs(i+1,cur+nums[i])
        #     sub=dfs(i+1,cur-nums[i])
        #     cache[i,cur] = add+sub
        #     return cache[i,cur]
        # return dfs(0,0)