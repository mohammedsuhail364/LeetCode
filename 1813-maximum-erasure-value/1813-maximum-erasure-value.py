class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        cur_sum=0
        res=0
        freq=set()
        for r in range(len(nums)):
            while nums[r] in freq:
                cur_sum-=nums[l]
                freq.remove(nums[l])
                l+=1    
            cur_sum+=nums[r]
            freq.add(nums[r])
            res=max(res,cur_sum)
        return res
