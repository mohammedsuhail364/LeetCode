class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=0
        min_diff=inf
        for i in range(len(nums)):
            l=i+1
            h=len(nums)-1
            while l<h:
                total=(nums[i]+nums[l]+nums[h])
                diff=abs(target-total)
                if diff<min_diff:
                    res=total
                    min_diff=diff
                if total<target:
                    l+=1
                else:
                    h-=1
        return res
