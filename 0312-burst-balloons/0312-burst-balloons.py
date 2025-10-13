class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # refer neetcode and take u forward

        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[0]*(n+2) for _ in range(n+2)]
        for l in range(n,0,-1):
            for r in range(1,n-1):
                if l>r:continue
                best=0
                for i in range(l,r+1):
                    coins=nums[l-1]*nums[i]*nums[r+1]
                    coins+=(dp[l][i-1]+dp[i+1][r])
                    best=max(best,coins)
                dp[l][r]=best
        return dp[1][n-2]
        