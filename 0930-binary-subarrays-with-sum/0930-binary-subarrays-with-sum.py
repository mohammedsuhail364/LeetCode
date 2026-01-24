class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def subarrayLessThanOrEqualToGoal(goal):
            res=0
            cur_sum=0
            l=0
            for r in range(len(nums)):
                cur_sum+=nums[r]
                while l<=r and cur_sum>goal:
                    cur_sum-=nums[l]
                    l+=1
                res+=(r-l+1) 
            return res
        return subarrayLessThanOrEqualToGoal(goal)-subarrayLessThanOrEqualToGoal(goal-1)