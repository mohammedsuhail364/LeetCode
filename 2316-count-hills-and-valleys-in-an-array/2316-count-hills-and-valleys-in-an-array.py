class Solution:
    def countHillValley(self, nums) -> int:
        n=len(nums)
        res=0
        i=0
        seen=set()
        while i<n:
            if i==0 or i==n-1:
                i+=1
                continue
            j=i-1
            k=i+1
            while j>-1 and nums[j]==nums[i]:
                j-=1 
            if j<0:
                i+=1
                continue
            while k<n and nums[k]==nums[i]:
                k+=1
            if k==n:
                i+=1
                continue
            if (nums[j]<nums[i]>nums[k] or nums[j]>nums[i]<nums[k]) and (j,k) not in seen:
                res+=1
                seen.add((j,k))
            i+=1
        return res
        