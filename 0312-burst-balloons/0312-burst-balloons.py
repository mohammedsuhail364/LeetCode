class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # refer neetcode
        nums=[1]+nums+[1]
        n=len(nums)
        memo={}
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in memo:
                return memo[l,r]
            best=0
            for i in range(l,r+1):
                coins=nums[l-1]*nums[i]*nums[r+1]
                coins+=(dfs(l,i-1)+dfs(i+1,r))
                best=max(best,coins)
            memo[l,r]=best
            return memo[l,r]
        return dfs(1,n-2)