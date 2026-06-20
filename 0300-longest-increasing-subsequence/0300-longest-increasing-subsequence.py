class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for prev in range(i-1,-2,-1): 
                # Why prev ranges from -1 to i-1
                # Think about what prev means in the memo solution:
                # dfs(i, prev)  # prev = index of last taken element
                p=prev+1 # why because of we cannot use the -1 as index so we can convert -1 into 1
                # skip the current one
                dp[i][p]=dp[i+1][p]
                # include the current one
                if prev==-1 or (prev!=-1 and nums[i]>nums[prev]):
                    dp[i][p]=max(dp[i][p],1+dp[i+1][i+1])
        return dp[0][0]

        cache={}
        def dfs(i,prev):
            if (i,prev) in cache:
                return cache[i,prev]
            if i>=len(nums):
                return 0
            # skip the current one
            cache[i,prev]=dfs(i+1,prev)
            # include the current one
            if prev==-1 or (prev!=-1 and nums[i]>nums[prev]):
                cache[i,prev]=max(cache[i,prev],(1+dfs(i+1,i)))
            return cache[i,prev]
        return dfs(0,-1)