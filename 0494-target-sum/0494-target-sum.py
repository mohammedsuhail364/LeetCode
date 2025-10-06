class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # refer neetcode 
        dp=defaultdict(int)
        dp[0]=1
        for i in range(len(nums)): # i refers to the sum like go through the target
            next_dp=defaultdict(int)
            for cur_sum,count in dp.items():
                next_dp[cur_sum+nums[i]]+=count
                next_dp[cur_sum-nums[i]]+=count
            dp=next_dp
        return dp[target]