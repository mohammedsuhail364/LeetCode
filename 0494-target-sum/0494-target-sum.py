class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def backtrack(i,cur_sum):
            if (i,cur_sum) in dp:
                return dp[(i,cur_sum)]
            if(i==len(nums)):
                return cur_sum==target
            
            dp[(i,cur_sum)] =(backtrack(i+1,cur_sum+nums[i])+backtrack(i+1,cur_sum-nums[i]))
            return dp[(i,cur_sum)]

        return backtrack(0,0)