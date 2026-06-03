class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # when convert to memo -> dp follow these steps
        # identify the states dfs(i,cur)-> dp[i][cur]
        n=len(nums)
        total=sum(nums)
        target=total//2
        dp=[[False]*(target+1) for _ in range(n+1)]
        if total%2!=0:
            return False
        # identify the base cases
        # i>=n or cur>total-cur -> False
        # cur==total-cur -> True
        for i in range(n+1):
            dp[i][target]=True
        for i in range(n-1,-1,-1):
            for cur in range(target):
                if cur>total-cur:
                    dp[i][cur]=False
                else:
                    skip=dp[i+1][cur]
                    include=dp[i+1][cur+nums[i]] if cur+nums[i]<=target else False
                    dp[i][cur]=skip or include
        return dp[0][0]
