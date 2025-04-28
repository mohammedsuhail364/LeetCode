class Solution:
    def countSubarrays(self, nums, k: int) -> int:
        cur_sum=0
        length=0
        l=0
        res=0
        for r in range(len(nums)):
            cur_sum+=nums[r]
            length+=1
            score=cur_sum*length
            while score>=k:
                cur_sum-=nums[l]
                length-=1
                l+=1
                score=cur_sum*length
            res+=length
        return res