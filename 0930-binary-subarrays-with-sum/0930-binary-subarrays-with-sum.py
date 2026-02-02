class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def findSumLessThanK(k):
            l=0
            res=0
            cur_sum=0
            for r in range(len(nums)):
                cur_sum+=nums[r]
                while l<=r and cur_sum>k:
                    cur_sum-=nums[l]
                    l+=1
                res+=(r-l+1)
            return res
        return findSumLessThanK(goal)-findSumLessThanK(goal-1)

        