class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_val=inf
        res=0
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                cur=nums[i]+nums[l]+nums[r]
                diff=abs(target-cur)
                if diff<min_val:
                    print((nums[i],nums[l],nums[r]))
                    res=cur
                    min_val=diff
                if cur>target:
                    r-=1
                else:
                    l+=1
        return res
