class Solution:
    def maximumTripletValue(self, nums) -> int:
        prefix_max=nums[0]
        max_difference=0
        res=0
        for k in range(1,len(nums)):
            val=max_difference*nums[k]
            res=max(res,val)
            if prefix_max<nums[k]:
                prefix_max=nums[k]
            max_difference=max(max_difference,prefix_max-nums[k])
        return res