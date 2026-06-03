class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        memo={}
        def dfs(i,cur_sum):
            if (i,cur_sum) in memo:
                return memo[i,cur_sum]
            if i>=len(nums) or cur_sum>total-cur_sum:
                return False
            if cur_sum==total-cur_sum:
                return True
            memo[i,cur_sum]= dfs(i+1,cur_sum) or dfs(i+1,cur_sum+nums[i])
            return memo[i,cur_sum]
        return dfs(0,0)