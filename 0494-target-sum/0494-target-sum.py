class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=[defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0]=1
        for i in range(len(nums)):
            for cur_sum,count in dp[i].items():
                dp[i+1][cur_sum+nums[i]]+=count
                dp[i+1][cur_sum-nums[i]]+=count
        return dp[len(nums)][target]




        dp={}
        def backtrack(i,cur_sum):
            if (i,cur_sum) in dp:
                return dp[(i,cur_sum)]
            if(i==len(nums)):
                return cur_sum==target
            
            dp[(i,cur_sum)] =(backtrack(i+1,cur_sum+nums[i])+backtrack(i+1,cur_sum-nums[i]))
            return dp[(i,cur_sum)]

        return backtrack(0,0)