class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_val=inf
        value=inf
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                val=nums[i]+nums[l]+nums[r]
                if abs(val-target)<min_val:
                    min_val=abs(val-target)
                    value=val
                if val<target:
                    l+=1
                else:
                    r-=1
        return value
        
        